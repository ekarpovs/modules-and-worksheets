'''
Bluring operation
'''
import cv2


def avg(step, **kwargs):
  '''
  Performs average bluring.

  Keyword arguments:
  - image: an image;

  Step arguments (--Type:Domain:[Possible Values]:Default-- name: description):
  --n;l;[3,5,7,9];3-- k: kernel size
  
  Returns:
  - image: result image;
  '''

  kernel = step.get('k', 3)
  kX = kY = kernel 

  kwargs['image'] = cv2.blur(kwargs['image'], (kX, kY)) 

  return kwargs



def gaus(step, **kwargs):
  '''
  Performs gausian bluring.

  Keyword arguments:
  - image: an image;

  Step arguments (--Type:Domain:[Possible Values]:Default-- name: description):
  --n;l;[3,5,7,9];3-- k: kernel size
  
  Returns:
  - image: result image;
  '''

  kernel = step.get('k', 3)
  kX = kY = kernel 

  kwargs['image'] = cv2.GaussianBlur(kwargs['image'], (kX, kY), 0)

  return kwargs



def median(step,**kwargs):
  '''
  Performs median bluring.

  Keyword arguments:
  - image: an image;

  Step arguments (--Type:Domain:[Possible Values]:Default-- name: description):
  --n;l;[3,5,7,9];3-- k: kernel size
  
  Returns:
  - image: result image;
  '''

  kernel = step.get('k', 3)

  kwargs['image'] = cv2.medianBlur(kwargs['image'], kernel)

  return kwargs
