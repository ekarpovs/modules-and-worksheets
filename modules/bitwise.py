'''
Bitwise operations
'''
import cv2


def btw_and(step, **kwargs):
  '''
  AND operation with an image and a mask.

  Keyword arguments:
  - image: an image;
  - mask: a mask.
  
  Returns:
  - image: the result image;
  '''

  kwargs['image'] = cv2.bitwise_and(kwargs.get('image'), kwargs.get('mask')) 

  return kwargs



def btw_or(step, **kwargs):
  '''
  OR operation with an image and a mask.

  Keyword arguments:
  - image: an image;
  - mask: a mask.
  
  Returns:
  - image: the result image;
  '''
  kwargs['image'] = cv2.bitwise_or(kwargs.get('image'), kwargs.get('mask')) 

  return kwargs



def btw_xor(step, **kwargs):
  '''
  XOR operation with an image and a mask.

  Keyword arguments:
  - image: an image;
  - mask: a mask.
  
  Returns:
  - image: the result image;
  '''

  kwargs['image'] = cv2.bitwise_xor(kwargs.get('image'), kwargs.get('mask')) 

  return kwargs



def btw_not(step, **kwargs):
  '''
  NOT operation with an image and a mask.

  Keyword arguments:
  - image: an image;
  - mask: a mask.
  
  Returns:
  - image: the result image;
  '''
  kwargs['image'] = cv2.bitwise_not(kwargs.get('image'), kwargs.get('mask')) 
   
  return kwargs