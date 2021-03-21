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
  - btwand: result image;
  '''

  btwand = cv2.bitwise_and(kwargs['image'], kwargs['image1']) 

  kwargs['btwand'] =  btwand

  return kwargs


def btw_or(**kwargs):
  '''
  Performs OR operation.

  Keyword arguments:
  - image: the first image;
  - image1: the second image.
  
  Returns:
  - btwor: result image;
  '''
  btwor = cv2.bitwise_or(kwargs['image'], kwargs['image1']) 

  kwargs['btwor'] =  btwor

  return kwargs


def btw_xor(**kwargs):
  '''
  Performs XOR operation.

  Keyword arguments:
  - image: the first image;
  - image1: the second image.
  
  Returns:
  - btwxor: result image;
  '''

  btwxor = cv2.bitwise_xor(kwargs['image'], kwargs['image1']) 

  kwargs['btwxor'] =  btwxor

  return kwargs


def btw_not(**kwargs):
  '''
  Performs NOT operation.

  Keyword arguments:
  - image: the first image;
  - image1: the second image.
  
  Returns:
  - btwnot: result image;
  '''
  btwbnot = cv2.bitwise_not(kwargs['image'], kwargs['image1']) 
  
  kwargs['btwnot'] = btwbnot
  
  return kwargs