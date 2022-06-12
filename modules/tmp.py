'''
Temporary solutions - will decollated an implemented as worksheets
'''

from typing import Dict
import cv2
import numpy as np


def skeleton(params: Dict , **data: Dict) -> Dict:
  '''
  Creates binary image.

  Parameters:
    - params:
      type: Dict[str,int](BINARY:0,BINARY_INV:1,TRUNC:2,TOZERO:3,TOZERO_INV:4)=BINARY; thresholding type cv2.THRES_(..)
      thrsh: Scale[int](0,255,1,0)=75; threshold
      otsu: bool=False; flag to use Otsu algorithm to choose the optimal threshold value
      shape: Dict[str,int](RECT:0,CROSS:1,ELLIPSE:2)=CROSS; shape of structuring element cv2.MORPH_(...)
      kernel: Scale[int](3,13,1,1)=3; kernel size
    - data: 
      image: ndarray; an image
  Returns:
    - data:
      skeleton: ndarray; the result binary image
  '''
  type = params.get('type', cv2.THRESH_BINARY)
  threshold = params.get('thrsh', 75)
  max_val = params.get('max-val', 255)
  otsu = params.get('otsu', False)
  shape = params.get('shape',cv2.MORPH_CROSS)
  kernel_size = params.get('kernel', 3)

  if otsu:
    type |= cv2.THRESH_OTSU
    threshold = 0

  image = data.get('image')

  size = np.size(image)
  skel = np.zeros(image.shape, np.uint8)

  (T, image) = cv2.threshold(image, threshold, max_val, type)

  elem = cv2.getStructuringElement(shape, ksize=(kernel_size, kernel_size))

  zeros = size
  done = False
  while( not done):
    eroded = cv2.erode(image, elem)
    temp = cv2.dilate(eroded, elem)
    temp = cv2.subtract(image, temp)
    skel = cv2.bitwise_or(skel, temp)
    image = eroded.copy()   
    zeros = size - cv2.countNonZero(image)   
    if zeros==size or zeros<=0:
        done = True

  (h, w) = skel.shape[:2]
  data['skeleton'] = skel
  return data


def gabor_filter(params: Dict , **data: Dict) -> Dict:
  '''
  Create and apply gabor filter.
  https://minhng.info/tutorials/gabor-filters-opencv.html

  Parameters:
    - params:   
      pidiv: Scale[int](1,18,1,0)=1; PI devider
      numkernels: Scale[int](1,20,1,0)=8; number of kernels
      ksize: Scale[int](3,128,1,0)=3; size of the filter returned.
      sigma: Scale[int](0,10,1,0)=3; standard deviation of the gaussian envelope.
      lambd: Scale[int](5,25,1,0)=5; Wavelength of the sinusoidal factor.
      psi:  Scale[float](0.0,5.0,0.1,0.0)=0.0; phase offset.
      gamma: Scale[float](0.05,1.0,0.05,0)=0; spatial aspect ratio
      ktype: Dict[str,int](CV_32F:5,CV_64F:6)=CV_32F; type of filter coefficients. It can be CV_32F or CV_64F .
      ddepth: Dict[str,int](SAME:-1,CV_8UC1:0,CV_8UC3:16,CV_32S:4,CV_32F:5,CV_64F:6)=SAME; -1 will give the output image depth as same as the input image.
    - data: 
      image: ndarray; the image
  Returns:
    - data:
      imstack: ndarray; the new images stack
  '''

  pi_div = params.get('pidiv', 1)
  num_kernels = params.get('numkernels', 8)
  ksize = params.get('ksize', 3)
  sigma = params.get('sigma', 3)
  theta = params.get('theta', 0)
  lambd = params.get('lambd', 5)
  psi = params.get('psi', 0.0)
  gamma = params.get('gamma', 0)
  ktype = params.get('ktype', cv2.CV_32F)
  ddepth = params.get('ddepth', -1)
  
  image= data.get('image')
  shape = image.shape
  shape_len = len(shape) 

  # geenrate gabor bank
  bank = []
  theta = 0 # orientation of the normal to the parallel stripes of a Gabor function
  step = np.pi / (num_kernels*pi_div)
  for idx in range(num_kernels):
    theta = idx * step
    # print('theta', np.rad2deg(theta))
    kernel = cv2.getGaborKernel(ksize=(ksize,ksize), sigma=sigma, theta=theta, lambd=lambd, gamma=gamma, psi=psi)
    bank.append(kernel)
 
  # create iamge stack and place to it the original image
  if shape_len >= 3:
    h, w, c = shape
    im_stack = np.zeros([h, w*(len(bank)+1), c])
    im_stack[:, :w, :] = image
  else:
    h, w = shape
    im_stack = np.zeros([h, w*(len(bank)+1)])
    im_stack[:, :w] = image


  for idx, kernel in enumerate(bank):
    # apply sliding window on 1(3) channel(s)
    if shape_len >= 3:
      layer_blue = cv2.filter2D(src=image[:,:,0], ddepth=ddepth, kernel=kernel)
      layer_green = cv2.filter2D(src=image[:,:,1], ddepth=ddepth, kernel=kernel)
      layer_red = cv2.filter2D(src=image[:,:,2], ddepth=ddepth, kernel=kernel)    
        
      new_image = np.zeros(list(layer_blue.shape) + [3], dtype='uint8')
      new_image[:,:,0], new_image[:,:,1], new_image[:,:,2] = layer_blue, layer_green, layer_red
      # place the new image into the stack
      im_stack[:, (idx+1)*w:(idx+2)*w, :] = new_image
    else:
      new_image = cv2.filter2D(src=image, ddepth=ddepth, kernel=kernel)
      # place the new image into the stack
      im_stack[:, (idx+1)*w:(idx+2)*w] = new_image

    # scale the kernel to 0-255
    kh, kw = kernel.shape[:2]
    min_val = np.min(kernel)
    max_val = np.max(kernel)
    new_kernel = (kernel - min_val) / (max_val - min_val) # 0-1
    new_kernel *= 255
  
    # place the new_image to the stack
    if shape_len >= 3:
      im_stack[:kh, (idx+1)*w:(idx+1)*w+kw, :] = np.repeat(np.expand_dims(new_kernel, axis=2), repeats=3, axis=2)
    else:
      im_stack[:kh, (idx+1)*w:(idx+1)*w+kw] = np.repeat(new_kernel, repeats=1, axis=1)

  # convert dtype from float64 to uint8
  im_stack = cv2.normalize(src=im_stack, dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

  data['imstack'] = im_stack
  return data
