'''
Gradient and edge dectection operations
Gradient magnitude and orientation.
'''
import cv2

def sobel(**kwargs):
  """
  direction 
  x 0
  y 1 
  """

  direction = kwargs.get('d', 0)
  dx = 1
  dy = 0
  if direction == 1:
    dx = 0
    dy = 1

  # compute gradients along the X or Y axis
  g = cv2.Sobel(kwargs['image'], ddepth=cv2.CV_64F, dx=dx, dy=dy) 
  # images are now of the floating point data type,
  # so convert them back a to unsigned 8-bit integer representation
  kwargs['image'] = cv2.convertScaleAbs(g)

  return kwargs


# compute a "wide", "mid-range", and "tight" threshold for the edges
def canny(**kwargs):
  """
  wide, mid, tight
  threshold1 10, 30, 240
  threshold2 200, 150, 250
  """

  threshold1 = kwargs.get('thrs1', 10)
  threshold2 = kwargs.get('thrs2', 200)

  kwargs['image'] = cv2.Canny(kwargs['image'], threshold1, threshold2)
  
  return kwargs