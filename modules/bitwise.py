'''
Bitwise operations:
btw_and: AND operation with the first image and the second one
btw_or: OR operation with the first image and the second one
btw_xor: XOR operation with the first image and the second one
btw_not: NOT operation with the first image and the second one
'''

from typing import Dict
import cv2


def btw_and(params: Dict , **data: Dict) -> Dict:
  '''
  AND operation with the first image and the second one.

  Parameters:
    - params:   
    - data: 
      image: ndarray; an image
      mask: ndarray; an mask
  Returns:
    - data:
      image: ndarray; the result image
  '''

  image = data.get('image')
  mask = data.get('mask')

  image = cv2.bitwise_and(image, mask) 

  data['image'] = image  

  return data

def btw_or(params: Dict , **data: Dict) -> Dict:
  '''
  OR operation with the first image and the second one.

  Parameters:
    - params:   
    - data: 
      image: ndarray; an image
      mask: ndarray; an mask
  Returns:
    - data:
      image: ndarray; the result image
  '''

  image = data.get('image')
  mask = data.get('mask')

  image = cv2.bitwise_or(image, mask) 

  data['image'] = image  
  return data

def btw_xor(params: Dict , **data: Dict) -> Dict:
  '''
  XOR operation with the first image and the second one.

  Parameters:
    - params:   
    - data: 
      image: ndarray; an image
      mask: ndarray; an mask
  Returns:
    - data:
      image: ndarray; the result image
  '''

  image = data.get('image')
  mask = data.get('mask')

  image = cv2.bitwise_xor(image, mask) 

  data['image'] = image
  return data

def btw_not(params: Dict , **data: Dict) -> Dict:
  '''
  NOT operation with the first image and the second one.

  Parameters:
    - params:   
    - data: 
      image: ndarray; an image
      mask: ndarray; an mask
  Returns:
    - data:
      image: ndarray; the result image
  '''

  image = data.get('image')
  mask = data.get('mask')

  image = cv2.bitwise_not(image, mask) 

  data['image'] = image
  return data

