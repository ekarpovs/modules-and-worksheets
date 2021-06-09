'''
Arithmetic operations
'''
import cv2
import numpy as np 


def arth_add(step, **kwargs):
  '''
  Performs Add operation - increase the intensity of all pixels in an image by 'ifact'.

  Keyword arguments:
  - image: an image;

  Step arguments (--Type:Domain:[Possible Values]:Default-- name: description):
  --n;s;[];1-- ifact: increase factor

  Returns:
  - image: result image;
  '''

  ifact = step.get('ifact', 1)

  # Create matrix (filled with ones) and the multiplying it by 'ifact' to create an
  # array filled with ifact value's, then add the images together; 
  # the image will "brighter"
  M = np.ones(kwargs['image'].shape, dtype = "uint8") * ifact
  kwargs['image'] = cv2.add(kwargs['image'], M) 

  return kwargs


def arth_sub(step, **kwargs):
  '''
  Performs Substraction operation - decrease the intensity of all pixels in an image by 'dfact'.

  Keyword arguments:
  - image: an image;

  Step arguments (--Type:Domain:[Possible Values]:Default-- name: description):
  --n;s;[];1-- dfact: decrease factor

  Returns:
  - image: result image;
  '''

  dfact = step.get('dfact', 1)

  # Create matrix (filled with ones) and the multiplying it by 'ifact' to create an
  # array filled with ifact value's, then add the images together; 
  # the image will "brighter"
  M = np.ones(kwargs['image'].shape, dtype = "uint8") * dfact
  kwargs['image'] = cv2.subtract(kwargs['image'], M) 

  return kwargs
