'''
Bitwise operations
'''
import cv2


def btw_and(params, **data):
  '''
  AND operation with the first image and the second one.

  Parameters:
    - params:   
    - data: 
      image: np.dtype; an image
      mask: np.dtype; an mask
  Returns:
    - data:
      image: np.dtype; the result image
  '''

  image = data.get('image')
  mask = data.get('mask')

  data['image'] = cv2.bitwise_and(image, mask) 
  return data

def btw_or(params, **data):
  '''
  OR operation with the first image and the second one.

  Parameters:
    - params:   
    - data: 
      image: np.dtype; an image
      mask: np.dtype; an mask
  Returns:
    - data:
      image: np.dtype; the result image
  '''

  image = data.get('image')
  mask = data.get('mask')

  data['image'] = cv2.bitwise_or(image, mask) 
  return data

def btw_xor(params, **data):
  '''
  XOR operation with the first image and the second one.

  Parameters:
    - params:   
    - data: 
      image: np.dtype; an image
      mask: np.dtype; an mask
  Returns:
    - data:
      image: np.dtype; the result image
  '''

  image = data.get('image')
  mask = data.get('mask')

  data['image'] = cv2.bitwise_xor(image, mask) 
  return data

def btw_not(params, **data):
  '''
  NOT operation with the first image and the second one.

  Parameters:
    - params:   
    - data: 
      image: np.dtype; an image
      mask: np.dtype; an mask
  Returns:
    - data:
      image: np.dtype; the result image
  '''

  image = data.get('image')
  mask = data.get('mask')

  data['image'] = cv2.bitwise_not(image, mask) 
  return data

