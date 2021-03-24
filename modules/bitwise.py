'''
Bitwise operations
'''
import cv2


def btw_and(step, **kwargs):
  '''
  Performs AND operation.

  Keyword arguments:
  - image: the first image;
  - image1: the second image.
  
  Returns:
  - image: result image;
  '''

  kwargs['image'] = cv2.bitwise_and(kwargs['image'], kwargs['image1']) 

  return kwargs



def btw_or(step, **kwargs):
  '''
  Performs OR operation.

  Keyword arguments:
  - image: the first image;
  - image1: the second image.
  
  Returns:
  - image: result image;
  '''
  kwargs['image'] = cv2.bitwise_or(kwargs['image'], kwargs['image1']) 

  return kwargs



def btw_xor(step, **kwargs):
  '''
  Performs XOR operation.

  Keyword arguments:
  - image: the first image;
  - image1: the second image.
  
  Returns:
  - image: result image;
  '''

  kwargs['image'] = cv2.bitwise_xor(kwargs['image'], kwargs['image1']) 

  return kwargs



def btw_not(step, **kwargs):
  '''
  Performs NOT operation.

  Keyword arguments:
  - image: the first image;
  - image1: the second image.
  
  Returns:
  - image: result image;
  '''
  kwargs['image'] = cv2.bitwise_not(kwargs['image'], kwargs['image1']) 
   
  return kwargs