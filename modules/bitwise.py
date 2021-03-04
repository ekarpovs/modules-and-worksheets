'''
Bitwise operations
'''
import cv2

def btw_and(**kwargs):
  '''
  Performs AND operation.
  Gets via kwargs: 
    - image;
    - image1;
  Returns result image.
  '''  
  kwargs['image'] = cv2.bitwise_and(kwargs['image'], kwargs['image1']) 

  return kwargs


def btw_or(**kwargs):
  '''
  Performs OR operation.
  Gets via kwargs: 
    - image;
    - image1;
  Returns result image.
  '''  
  kwargs['image'] = cv2.bitwise_or(kwargs['image'], kwargs['image1']) 

  return kwargs


def btw_xor(**kwargs):
  '''
  Performs XOR operation.
  Gets via kwargs: 
    - image;
    - image1;
  Returns result image.
  '''  
  kwargs['image'] = cv2.bitwise_xor(kwargs['image'], kwargs['image1']) 

  return kwargs


def btw_not(**kwargs):
  '''
  Performs NOT operation.
  Gets via kwargs: 
    - image;
    - image1;
  Returns result image.
  '''  
  kwargs['image'] = cv2.bitwise_not(kwargs['image'], kwargs['image1']) 

  return kwargs