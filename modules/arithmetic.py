'''
Arithmetic operations
'''
import cv2
import numpy as np 


def arth_add(step, **kwargs):
  '''
  Performs Add operation with the input image and a mask

  Keyword arguments:
  - image: an image;
  - mask: a mask;

  Step arguments (--Type:Domain:[Possible Values]:Default-- name: description):

  Returns:
  - image: result image;
  '''

  mask = kwargs.get('mask')

  kwargs['image'] = cv2.add(kwargs.get('image'), mask) 

  return kwargs


def arth_sub(step, **kwargs):
  '''
  Performs Substraction operation with the input image and a mask

  Keyword arguments:
  - image: an image;
  - mask: a mask;

  Step arguments (--Type:Domain:[Possible Values]:Default-- name: description):
  --n;s;[];1-- dfact: decrease factor

  Returns:
  - image: result image;
  '''

  mask = kwargs.get('mask')

  kwargs['image'] = cv2.subtract(kwargs.get('image'), mask) 

  return kwargs
