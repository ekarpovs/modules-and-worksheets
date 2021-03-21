'''
Bluring operation
'''
import cv2

def avg(**kwargs):
  '''
  Performs average bluring.

  Keyword arguments (key, default):
  - image: an image;
  - k: kernel size, 3.
  
  Returns:
  - blravg: result image;
  '''

  kernel = kwargs.get('k', 3)
  kX = kY = kernel 

  blravg = cv2.blur(kwargs['image'], (kX, kY)) 

  kwargs['blravg'] = blravg


  return kwargs


def gaus(**kwargs):
  '''
  Performs gausian bluring.

  Keyword arguments (key, default):
  - image: an image;
  - k: kernel size, 3.
  
  Returns:
  - blrgaus: result image;
  '''

  kernel = kwargs.get('k', 3)
  kX = kY = kernel 

  blrgaus = cv2.GaussianBlur(kwargs['image'], (kX, kY), 0)

  kwargs['blrgaus'] = blrgaus

  return kwargs


def median(**kwargs):
  '''
  Performs median bluring.

  Keyword arguments (key, default):
  - image: an image;
  - k: kernel size, 3.
  
  Returns:
  - blrmedian: result image;
  '''

  kernel = kwargs.get('k', 3)

  blrmedian = cv2.medianBlur(kwargs['image'], kernel)

  kwargs['blrmedian'] = blrmedian

  return kwargs
