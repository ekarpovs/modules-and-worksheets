'''
Bluring operation
'''
import cv2

def avg(**kwargs):
  '''
  Performs average bluring.
  Gets via kwargs (key, default value): 
    - image;
    - k - kernel size, 3.
  Returns result image.
  '''  

  kernel = kwargs.get('k', 3)
  kX = kY = kernel 

  kwargs['image'] = cv2.blur(kwargs['image'], (kX, kY)) 

  return kwargs


def gaus(**kwargs):
  '''
  Performs gausian bluring.
  Gets via kwargs (key, default value): 
    - image;
    - k - kernel size, 3.
  Returns result image.
  '''  

  kernel = kwargs.get('k', 3)
  kX = kY = kernel 

  kwargs['image'] = cv2.GaussianBlur(kwargs['image'], (kX, kY), 0)

  return kwargs


def median(**kwargs):
  '''
  Performs median bluring.
  Gets via kwargs (key, default value): 
    - image;
    - k - kernel size, 3.
  Returns result image.
  '''  

  kernel = kwargs.get('k', 3)

  kwargs['image'] = cv2.medianBlur(kwargs['image'], kernel)

  return kwargs
