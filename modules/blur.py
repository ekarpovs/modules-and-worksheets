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
      kernel: List[int](3,5,7,9)=3; kernel size
    - data: 
      image: np.dtype; the image
  Returns:
    - data:
      image: np.dtype; the blured image
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
      kernel: List[int](3,5,7,9)=3; kernel size
    - data: 
      image: np.dtype; the image
  Returns:
    - data:
      image: np.dtype; the blured image
  '''

  kernel = params.get('kernel', 3)
  kX = kY = kernel 
  data['image'] = cv2.GaussianBlur(data.get('image'), (kX, kY), 0) 
  return data

def median(params: Dict , **data: Dict) -> Dict:
  '''
  Median bluring.

  Parameters:
    - params:   
      kernel: List[int](3,5,7,9)=3; kernel size
    - data: 
      image: np.dtype; the image
  Returns:
    - data:
      image: np.dtype; the blured image
  '''

  kernel = params.get('kernel', 3)
  data['image'] = cv2.medianBlur(data.get('image'), kernel) 
  return data

def bilateral(params: Dict , **data: Dict) -> Dict:
  '''
  Bilateral bluring.

  Parameters:
    - params:   
      d: List[int](7,9,11,15,17,19,21,23,25,27)=11; diameter of each pixel neighborhood
      sigmacolor: int=17; filter sigma in the color space.
      sigmaspace: int=17; filter sigma in the coordinate space.
      border: Dict[str,int](DEFAULT:4,REFLECT:2,REFLECT101:4,REFLECT_101:4,REPLICATE:1,TRANSPARENT:5,WRAP:3)=DEFAULT; pixel extrapolation method cv2.BORDER_(...)
    - data: 
      image: np.dtype; the image
  Returns:
    - data:
      image: np.dtype; the blured image
  '''

  d = params.get('d', 11)
  sigma_color = params.get('sigmacolor', 17)
  sigma_space = params.get('sigmaspace', 17)
  border_type = params.get('border',cv2.BORDER_DEFAULT) # Pixel extrapolation method

  data['image'] = cv2.bilateralFilter(data.get('image'), d, sigma_color, sigma_space, border_type) 
  return data
