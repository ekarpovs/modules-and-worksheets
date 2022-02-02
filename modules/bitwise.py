'''
Bitwise operations
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
      shape: Dict[str, int]; the shape of the image
  '''

  image = data.get('image')
  mask = data.get('mask')

  image = cv2.bitwise_and(image, mask) 
  (h, w) = image.shape[:2]
  data['image'] = image  
  data['shape'] = {'shape': {'h': h, 'w': w}}
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
      shape: Dict[str, int]; the shape of the image
  '''

  image = data.get('image')
  mask = data.get('mask')

  image = cv2.bitwise_or(image, mask) 
  (h, w) = image.shape[:2]
  data['shape'] = {'shape': {'h': h, 'w': w}}
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
      shape: Dict[str, int]; the shape of the image
  '''

  image = data.get('image')
  mask = data.get('mask')

  image = cv2.bitwise_xor(image, mask) 
  (h, w) = image.shape[:2]
  data['image'] = image
  data['shape'] = {'shape': {'h': h, 'w': w}}
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
      shape: Dict[str, int]; the shape of the image
  '''

  image = data.get('image')
  mask = data.get('mask')

  image = cv2.bitwise_not(image, mask) 
  (h, w) = image.shape[:2]
  data['image'] = image
  data['shape'] = {'shape': {'h': h, 'w': w}}
  return data

