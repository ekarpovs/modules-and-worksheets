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
      sigma: Scale[int](0,10,1,0)=4; standard deviation of the gaussian envelope.
      small: bool=False; use small scaled theta
      theta: Scale[int](0,90,1,0)=0; orientation of the normal to the parallel stripes of a Gabor function.
      stheta: Scale[float](0.0,5.0,0.1,0.0)=0.0; small size orientation of the normal to the parallel stripes of a Gabor function.
      lambd: Scale[int](5,25,5,0)=5; Wavelength of the sinusoidal factor.
      psi:  Scale[float](0.0,5.0,0.1,0.0)=0.0; phase offset.
      gamma: Scale[int](0,100,10,0)=0; spatial aspect ratio
      ktype: Dict[str,int](CV_32F:5,CV_64F:6)=CV_32F; type of filter coefficients. It can be CV_32F or CV_64F .
    - data: 
      image: array[dtype[uint8]]; the image
  Returns:
    - data:
      image: array[dtype[uint8]]; the result image
      kernel: array[dtype[uint8]]; the kernel
  '''

  ksize = params.get('ksize', 3)
  sigma = params.get('sigma', 4)
  small = params.get('small', False)
  stheta = params.get('stheta', 0.0)
  theta = params.get('theta', 0)
  lambd = params.get('lambd', 5)
  psi = params.get('psi', 0.0)
  gamma = params.get('gamma', 0)
  ktype = params.get('ktype', cv2.CV_32F)

  if small:
    theta = stheta
  kernel = cv2.getGaborKernel((ksize, ksize), sigma, np.degrees(theta), lambd, psi, gamma, ktype)

  # f = np.fft.fft2(kernel)
  # fshift = np.fft.fftshift(f).astype(np.float32)
  # fshift = np.sqrt(np.power(fshift.imag,2)+np.power(fshift.real,2))
  # fshift = (fshift - np.min(fshift))/(np.max(fshift)-np.min(fshift))
  # kernel = fshift

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
      image: array[dtype[uint8]]; the image
      kernel: array[dtype[uint8]]; the kernel
  Returns:
    - data:
      image: array[dtype[uint8]]; the result image
  '''

  ddepth = params.get('ddepth', cv2.CV_32F)
  
  image= data.get('image')
  kernel= data.get('kernel')

  kernel = cv2.filter2D(image, ddepth, kernel)

  data['kernel'] = kernel
  return data

