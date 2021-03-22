'''
Bluring operation
'''
import cv2
from modules import flowoperation

@flowoperation
def avg(step, **kwargs):
  '''
  Performs average bluring.

  Keyword arguments (key, default):
  - image: an image;
  - k: kernel size, 3.
  
  Returns:
  - blravg: result image;
  '''

  kernel = step.get('k', 3)
  kX = kY = kernel 

  kwargs['image'] = cv2.blur(kwargs['image'], (kX, kY)) 

  return kwargs


@flowoperation
def gaus(step, **kwargs):
  '''
  Performs gausian bluring.

  Keyword arguments (key, default):
  - image: an image;
  - k: kernel size, 3.
  
  Returns:
  - blrgaus: result image;
  '''

  kernel = step.get('k', 3)
  kX = kY = kernel 

  kwargs['image'] = cv2.GaussianBlur(kwargs['image'], (kX, kY), 0)

  return kwargs


@flowoperation
def median(step,**kwargs):
  '''
  Performs median bluring.

  Keyword arguments (key, default):
  - image: an image;
  - k: kernel size, 3.
  
  Returns:
  - blrmedian: result image;
  '''

  kernel = step.get('k', 3)

  kwargs['image'] = cv2.medianBlur(kwargs['image'], kernel)

  return kwargs
