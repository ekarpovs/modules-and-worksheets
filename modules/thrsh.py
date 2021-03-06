'''
Threshold operations
'''
import cv2

def simple(**kwargs):
  '''
  Applies a fixed-level (or optimal) threshold to each array element.

  Keyword arguments (key, default):
  - image: an image;
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

  type = kwargs.get('type', cv2.THRESH_BINARY)
  threshold = kwargs.get('thrsh', 127)
  otsu = kwargs.get('otsu', False)

  if otsu:
    type |= cv2.THRESH_OTSU
    threshold = 0

  (T, kwargs['image']) = cv2.threshold(kwargs['image'], threshold, 255, type)

  return kwargs


def adaptive(**kwargs):
  '''
  Applies a fixed-level (or optimal) threshold to each array element.

  Keyword arguments (key, default):
  - image: an image;
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

  type = kwargs.get('type', cv2.THRESH_BINARY) 
  method = kwargs.get('mth', cv2.ADAPTIVE_THRESH_MEAN_C) 
  na = kwargs.get('na',15) # neighborhood area
  c = kwargs.get('c', 5) #  

  kwargs['image'] = cv2.adaptiveThreshold(kwargs['image'], 255, method, type, na, c)

  return kwargs
