'''
Arithmetic operations
'''

from typing import Dict
import cv2
import numpy as np 


def arth_add(params: Dict , **data: Dict) -> Dict:
  '''
  Adds the mask image to the image

  Parameters:
    - params:   
    - data: 
      image: np.dtype; the image
      mask: np.dtype; the second image
  Returns:
    - data:
      image: np.dtype; the result image
  '''
  
  image = data.get('image')
  mask = data.get('mask')
  data['image'] = cv2.add(image, mask) 
  return data


def arth_sub(params: Dict , **data: Dict) -> Dict:
  '''
  Substracts mask from the image

  Parameters:
    - params:   
    - data: 
      image: np.dtype ; the image
      mask: np.dtype; the second image
  Returns:
    - data:
      image: np.dtype; the result image
  '''

  image = data.get('image')
  mask = data.get('mask')
  data['image'] = cv2.subtract(image, mask) 
  return data


def arth_add_into(params: Dict , **data: Dict) -> Dict:
  '''
  Adds the mask into the image from defined X, Y offsets

  Parameters:
    - params:   
      offset-y: int=0; vertical offset
      offset-x: int=0; horizontal offset
    - data: 
      image: np.dtype; the image
      mask: np.dtype; the second image
  Returns:
    - data:
      image: np.dtype; the result image
  '''

  offset_y = params.get('offset-y', 0)
  offset_x = params.get('offset-x', 0)
  image = data.get('image')
  mask = data.get('mask')
  image[offset_y:offset_y + mask.shape[0], offset_x:offset_x + mask.shape[1]] = mask
  data['image'] = image
  return data
