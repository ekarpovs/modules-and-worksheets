'''
Gradient and edge dectection operations
Gradient magnitude and orientation.
'''
import cv2
import numpy as np


def sobel(step, **kwargs):
  '''
  Computes compute gradients along the X or Y axis uses Sobel algorithm.

  Keyword arguments:
  - image: an image;

  Step arguments (--Type:Domain:[Possible Values]:Default-- name: description):
  --n;d;[horizontal:0,vertical:1];horizontal-- direction: direction (x, y));

  Returns:
  - image: result image;
  '''

  direction = step.get('d', 0)
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



def canny(step, **kwargs):
  '''
  Computes a "wide", "mid-range", and "tight" threshold for the edges.

  Keyword arguments:
  - image: an image;

  Step arguments (--Type:Domain:[Possible Values]:Default-- name: description):
  --n;r;[10,150,1];50-- thrs1: threshold1;
  --n;r;[100,252,1];200-- thrs2: threshold2;

  Returns:
  - image: result image;
  '''

  threshold1 = step.get('thrs1', 10)
  threshold2 = step.get('thrs2', 200)

  kwargs['image'] = cv2.Canny(kwargs['image'], threshold1, threshold2)
 
  return kwargs



def laplacian(step, **kwargs):
  '''
  Computes the Laplacian of the image .

  Keyword arguments:
  - image: an image;

  Returns:
  - edgelap: result image;
  '''

  lap = cv2.Laplacian(kwargs['image'], cv2.CV_64F)
  kwargs['image'] = np.uint8(np.absolute(lap)) 

  return kwargs