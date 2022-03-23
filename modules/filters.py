'''
Filters
'''

from typing import Dict
import cv2
import numpy as np


def gabor_kernel(params: Dict , **data: Dict) -> Dict:
  '''
  Create gabor filter.

  Parameters:
    - params:   
      ksize: Scale[int](3,128,1,0)=3; size of the filter returned.
      sigma: Scale[int](0,10,1,0)=3; standard deviation of the gaussian envelope.
      theta: Scale[int](0,90,1,0)=0; orientation of the normal to the parallel stripes of a Gabor function.
      lambd: Scale[int](5,25,1,0)=5; Wavelength of the sinusoidal factor.
      psi:  Scale[float](0.0,5.0,0.1,0.0)=0.0; phase offset.
      gamma: Scale[int](0,100,10,0)=0; spatial aspect ratio
      ktype: Dict[str,int](CV_32F:5,CV_64F:6)=CV_32F; type of filter coefficients. It can be CV_32F or CV_64F .
    - data: 
  Returns:
    - data:
      kernel: ndarray; the kernel
  '''

  ksize = params.get('ksize', 3)
  sigma = params.get('sigma', 3)
  theta = params.get('theta', 0)
  lambd = params.get('lambd', 5)
  psi = params.get('psi', 0.0)
  gamma = params.get('gamma', 0)
  ktype = params.get('ktype', cv2.CV_32F)

  kernel = cv2.getGaborKernel((ksize, ksize), sigma, np.deg2rad(theta), lambd, psi, gamma, ktype)


  data['kernel'] = kernel
  return data

def filter_2d(params: Dict , **data: Dict) -> Dict:
  '''
  Changes the pixel intensity value of an image 
  based on the surrounding pixel intensity values.

  Parameters:
    - params:   
      ddepth: Dict[str,int](SAME:-1,CV_8UC1:0,CV_8UC3:16,CV_32S:4,CV_32F:5,CV_64F:6)=SAME; -1 will give the output image depth as same as the input image.
    - data: 
      image: ndarray; the image
      kernel: ndarray; the kernel
  Returns:
    - data:
      image: ndarray; the result image
  '''

  ddepth = params.get('ddepth', -1)
  
  image= data.get('image')
  kernel= data.get('kernel')
  shape_len = len(image.shape)
  if shape_len >= 3:
    layer_blue = cv2.filter2D(src=image[:,:,0], ddepth=ddepth, kernel=kernel)
    layer_green = cv2.filter2D(src=image[:,:,1], ddepth=ddepth, kernel=kernel)
    layer_red = cv2.filter2D(src=image[:,:,2], ddepth=ddepth, kernel=kernel)    
      
    new_image = np.zeros(list(layer_blue.shape) + [3], dtype='uint8')
    new_image[:,:,0], new_image[:,:,1], new_image[:,:,2] = layer_blue, layer_green, layer_red
  else:
    new_image = cv2.filter2D(src=image, ddepth=ddepth, kernel=kernel)

  data['image'] = new_image
  return data

