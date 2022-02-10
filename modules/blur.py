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
      image: ndarray; the image
  Returns:
    - data:
      image: ndarray; the blured image
      shape: Dict[str, int]; the shape of the image
  '''

  kernel = params.get('kernel', 3)
  kX = kY = kernel 
  image = data.get('image')

  blured = cv2.blur(image, (kX, kY)) 
  (h, w) = blured.shape[:2]
  data['image'] = blured
  data['shape'] = {'shape': {'h': h, 'w': w}}
  return data

def gaus(params: Dict , **data: Dict) -> Dict:
  '''
  Gaussian bluring.

  Parameters:
    - params:   
      kernel: Scale[int](3,13,1,1)=3; kernel size
    - data: 
      image: ndarray; the image
  Returns:
    - data:
      image: ndarray; the blured image
      shape: Dict[str, int]; the shape of the image
  '''

# ksize.width > 0 && ksize.width % 2 == 1 && ksize.height > 0 && ksize.height % 2 == 1
  kernel = params.get('kernel', 3)
  kX = kY = int(kernel) 

  image = data.get('image')
  blured = cv2.GaussianBlur(image, (kX, kY), 0)
  (h, w) = blured.shape[:2]
  data['image'] = blured
  data['shape'] = {'shape': {'h': h, 'w': w}}
  return data

def median(params: Dict , **data: Dict) -> Dict:
  '''
  Median bluring.

  Parameters:
    - params:   
      kernel: Scale[int](3,13,1,1)=3; kernel size
    - data: 
      image: ndarray; the image
  Returns:
    - data:
      image: ndarray; the blured image
      shape: Dict[str, int]; the shape of the image
  '''

  kernel = params.get('kernel', 3)

  image = data.get('image')

  blured = cv2.medianBlur(image, kernel)
  (h, w) = blured.shape[:2]
  data['image'] = blured
  data['shape'] = {'shape': {'h': h, 'w': w}}
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
      image: ndarray; the image
  Returns:
    - data:
      image: ndarray; the blured image
      shape: Dict[str, int]; the shape of the image
  '''

  d = params.get('d', 11)
  sigma_color = params.get('sigmacolor', 17)
  sigma_space = params.get('sigmaspace', 17)
  border_type = params.get('border',cv2.BORDER_DEFAULT) # Pixel extrapolation method

  image = data.get('image')

  blured = cv2.bilateralFilter(data.get('image'), d, sigma_color, sigma_space, border_type) 
  (h, w) = blured.shape[:2]
  data['image'] = blured
  data['shape'] = {'shape': {'h': h, 'w': w}}
  return data
