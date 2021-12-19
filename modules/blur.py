'''
Bluring operation
'''

import cv2
from typing import Dict


def avrg(params: Dict , **data: Dict) -> Dict:
  '''
  Average bluring.

  Parameters:
    - params:   
      kernel: Scale[int](3,13,1,1)=3; kernel size
    - data: 
      image: array[dtype[uint8]]; the image
  Returns:
    - data:
      image: array[dtype[uint8]]; the blured image
  '''

  kernel = params.get('kernel', 3)
  kX = kY = kernel 
  data['image'] = cv2.blur(data.get('image'), (kX, kY)) 
  return data

def gaus(params: Dict , **data: Dict) -> Dict:
  '''
  Gaussian bluring.

  Parameters:
    - params:   
      kernel: Scale[int](3,13,1,1)=3; kernel size
    - data: 
      image: array[dtype[uint8]]; the image
  Returns:
    - data:
      image: array[dtype[uint8]]; the blured image
  '''
# ksize.width > 0 && ksize.width % 2 == 1 && ksize.height > 0 && ksize.height % 2 == 1
  kernel = params.get('kernel', 3)
  kX = kY = int(kernel) 
  data['image'] = cv2.GaussianBlur(data.get('image'), (kX, kY), 0) 
  return data

def median(params: Dict , **data: Dict) -> Dict:
  '''
  Median bluring.

  Parameters:
    - params:   
      kernel: Scale[int](3,13,1,1)=3; kernel size
    - data: 
      image: array[dtype[uint8]]; the image
  Returns:
    - data:
      image: array[dtype[uint8]]; the blured image
  '''

  kernel = params.get('kernel', 3)
  data['image'] = cv2.medianBlur(data.get('image'), kernel) 
  return data

def bilateral(params: Dict , **data: Dict) -> Dict:
  '''
  Bilateral bluring.

  Parameters:
    - params:   
      d: Scale[int](7,27,1,1)=11; diameter of each pixel neighborhood
      sigmacolor: Scale[int](9,80,1,0)=17; filter sigma in the color space.
      sigmaspace: Scale[int](9,80,1,0)=17; filter sigma in the coordinate space.
      border: Dict[str,int](DEFAULT:4,REFLECT:2,REFLECT101:4,REFLECT_101:4,REPLICATE:1,TRANSPARENT:5,WRAP:3)=DEFAULT; pixel extrapolation method cv2.BORDER_(...)
    - data: 
      image: array[dtype[uint8]]; the image
  Returns:
    - data:
      image: array[dtype[uint8]]; the blured image
  '''

  d = params.get('d', 11)
  sigma_color = params.get('sigmacolor', 17)
  sigma_space = params.get('sigmaspace', 17)
  border_type = params.get('border',cv2.BORDER_DEFAULT) # Pixel extrapolation method

  data['image'] = cv2.bilateralFilter(data.get('image'), d, sigma_color, sigma_space, border_type) 
  return data
