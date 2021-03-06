'''
Bitwise operations
'''
import cv2

def btw_and(**kwargs):
  '''
  Performs AND operation.

  Keyword arguments:
  - image: the first image;
  - image1: the second image.
  
  Returns:
  - result image;
  - the kwargs as is.
  '''

  kwargs['image'] = cv2.bitwise_and(kwargs['image'], kwargs['image1']) 

  return kwargs


def btw_or(**kwargs):
  '''
  Performs OR operation.

  Keyword arguments:
  - image: the first image;
  - image1: the second image.
  
  Returns:
  - result image;
  - the kwargs as is.
  '''
  kwargs['image'] = cv2.bitwise_or(kwargs['image'], kwargs['image1']) 

  return kwargs


def btw_xor(**kwargs):
  '''
  Performs XOR operation.

  Keyword arguments:
  - image: the first image;
  - image1: the second image.
  
  Returns:
  - result image;
  - the kwargs as is.
  '''

  kwargs['image'] = cv2.bitwise_xor(kwargs['image'], kwargs['image1']) 

  return kwargs


def btw_not(**kwargs):
  '''
  Performs NOT operation.

  Keyword arguments:
  - image: the first image;
  - image1: the second image.
  
  Returns:
  - result image;
  - the kwargs as is.
  '''
  kwargs['image'] = cv2.bitwise_not(kwargs['image'], kwargs['image1']) 

  return kwargs