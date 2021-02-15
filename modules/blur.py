import cv2
# Bluring operation

def avg(**kwargs):

  kernel = kwargs.get('k', 3)
  kX = kY = kernel 

  kwargs['image'] = cv2.blur(kwargs['image'], (kX, kY)) 

  return kwargs


def gaus(**kwargs):

  kernel = kwargs.get('k', 3)
  kX = kY = kernel 
  kwargs.pop('k', None)

  kwargs['image'] = cv2.GaussianBlur(kwargs['image'], (kX, kY), 0)

  return kwargs


def median(**kwargs):

  kernel = kwargs.get('k', 3)
  kwargs.pop('k', None)

  kwargs['image'] = cv2.medianBlur(kwargs['image'], kernel)

  return kwargs
