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
      image: ndarray; the image
      mask: ndarray; the second image
  Returns:
    - data:
      image: ndarray; the result image
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
      image: ndarray ; the image
      mask: ndarray; the second image
  Returns:
    - data:
      image: ndarray; the result image
  '''

  image = data.get('image')
  mask = data.get('mask')
  data['image'] = cv2.subtract(image, mask) 
  return data


def arth_add_into(params: Dict , **data: Dict) -> Dict:
  '''
  Adds the image into the mask from defined X, Y offsets

  Parameters:
    - params:   
      offsety: int=0; vertical offset
      offsetx: int=0; horizontal offset
    - data: 
      image: ndarray; the image
      mask: ndarray; the second image
  Returns:
    - data:
      image: ndarray; the result image
  '''

  offset_y = params.get('offsety', 0)
  offset_x = params.get('offsetx', 0)
  image = data.get('image')
  mask = data.get('mask')
  mask[offset_y:offset_y + image.shape[0], offset_x:offset_x + image.shape[1]] = image
  data['image'] = mask
  return data


def arth_add_weighted(params: Dict , **data: Dict) -> Dict:
  '''
  Calculates the weighted sum of two arrays (images): image*alpha + mask*beta + gamma 

  Parameters:
    - params:   
      alpha: float=0.5; weight of the first array elements.
      beta: float=0.5; weight of the second array elements.
      gamma: float=0.0; scalar added to each sum
    - data: 
      image: ndarray; the image
      mask: ndarray; the second image
  Returns:
    - data:
      image: ndarray; the result image
  '''

  alpha = params.get('alpha', 0.5)
  beta = params.get('beta', 0.5)  
  gamma = params.get('gamma', 0.0)

  image = data.get('image')
  mask = data.get('mask')

  combined = cv2.addWeighted(image, alpha, mask, beta, gamma) 

  data['image'] = combined
  return data
