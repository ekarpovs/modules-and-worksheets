'''
Gradient and edge dectection operations
Gradient magnitude and orientation.
'''
import cv2
import numpy as np
from modules import flowoperation

@flowoperation
def sobel(**kwargs):
  '''
  Computes compute gradients along the X or Y axis uses Sobel algorithm.

  Keyword arguments (key, default):
  - image: an image;
  - direction: 
    - x: 0
    - y: 1 

  Returns:
  - edgesobel: result image;
  '''

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


@flowoperation
def canny(**kwargs):
  '''
  Computes a "wide", "mid-range", and "tight" threshold for the edges.

  Keyword arguments (key, default):
  - image: an image;
  - thrs1: threshold1;
  - thrs2: threshold2;

  Returns:
  - edgecanny: result image;
  '''

  threshold1 = kwargs.get('thrs1', 10)
  threshold2 = kwargs.get('thrs2', 200)

  kwargs['image'] = cv2.Canny(kwargs['image'], threshold1, threshold2)
 
  return kwargs


@flowoperation
def laplacian(**kwargs):
  '''
  Computes the Laplacian of the image .

  Keyword arguments (key, default):
  - image: an image;

  Returns:
  - edgelap: result image;
  '''

  lap = cv2.Laplacian(kwargs['image'], cv2.CV_64F)
  kwargs['image'] = np.uint8(np.absolute(lap)) 

  return kwargs