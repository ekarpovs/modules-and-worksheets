'''
Threshold operations
'''
import cv2


def simple(step, **kwargs):
  '''
  Applies a fixed-level (or optimal) threshold to each array element.

  Keyword arguments:
  - image: an image;

  Step arguments (key, default):
  - type: thresholding type, 0:
    - cv2.THRESH_BINARY: 0;
    - cv2.THRESH_BINARY_INV: 1;
    - cv2.THRESH_TRUNC: 2;
    - cv2.THRESH_TOZERO: 3;
    - cv2.THRESH_TOZERO_INV: 4;
  - thrsh: threshold value, 127;
  - otsu:  flag to use Otsu algorithm to choose the optimal threshold value, False

  Returns:
  - image: result binary image;
  '''

  type = step.get('type', cv2.THRESH_BINARY)
  threshold = step.get('thrsh', 127)
  otsu = step.get('otsu', False)

  if otsu:
    type |= cv2.THRESH_OTSU
    threshold = 0

  (T, thrsh) = cv2.threshold(kwargs['image'], threshold, 255, type)

  kwargs['image'] = thrsh

  return kwargs



def adaptive(step, **kwargs):
  '''
  Applies a fixed-level (or optimal) threshold to each array element.

  Keyword arguments:
  - image: an image;

  Step arguments (key, default):
  - type: thresholding type, 0:
    - cv2.THRESH_BINARY: 0;
    - cv2.THRESH_BINARY_INV: 1;
    - cv2.THRESH_TRUNC: 2;
    - cv2.THRESH_TOZERO: 3;
    - cv2.THRESH_TOZERO_INV: 4;
  - mth: adaptive thresholding algorithm to use, 0:
    - cv2.ADAPTIVE_THRESH_MEAN_C: 0;
    - cv2.ADAPTIVE_THRESH_GAUSSIAN_C: 1.
  - na: neighborhood area, 15;
  - c: a constant which is subtracted from the mean or weighted mean calculated, 5.

  Returns:
  - image: result binary image;
  '''

  type = step.get('type', cv2.THRESH_BINARY) 
  method = step.get('mth', cv2.ADAPTIVE_THRESH_MEAN_C) 
  na = step.get('na',15) # neighborhood area
  c = step.get('c', 5) #  

  thrsh = cv2.adaptiveThreshold(kwargs['image'], 255, method, type, na, c)

  kwargs['image'] = thrsh

  return kwargs
