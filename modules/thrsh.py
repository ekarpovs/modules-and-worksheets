'''
Threshold operations
'''
import cv2


def simple(step, **kwargs):
  '''
  Applies a fixed-level (or optimal) threshold to each array element.

  Keyword arguments:
  - image: an image;

  Step arguments (--Type:Domain:[Possible Values]:Default-- name: description):
  --n;d;[BINARY:0,BINARY_INV:1,TRUNC:2,TOZERO:3,TOZERO_INV:4];BINARY-- type: thresholding type cv2.THRES_(..)
  --n;r;[0,255];127-- thrsh: threshold value
  --b;f;[False,True];False-- otsu:  flag to use Otsu algorithm to choose the optimal threshold value

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

  Step arguments (--Type:Domain:[Possible Values]:Default-- name: description):
  --n;d;[BINARY:0,BINARY_INV:1,TRUNC:2,TOZERO:3,TOZERO_INV:4];BINARY-- type: thresholding type cv2.THRES_(...)
  --n;d;[MEAN_C:0,GAUSSIAN_C:1];MEAN_C-- meth: adaptive thresholding algorithm to use cv2.ADAPTIVE_THRESH_(...)
  --n;s;[];15-- na: neighborhood area
  --n;s;[];5-- c: a constant which is subtracted from the mean or weighted mean calculated

  Returns:
  - image: result binary image;
  '''

  type = step.get('type', cv2.THRESH_BINARY) 
  method = step.get('meth', cv2.ADAPTIVE_THRESH_MEAN_C) 
  na = step.get('na',15) # neighborhood area
  c = step.get('c', 5) #  

  thrsh = cv2.adaptiveThreshold(kwargs['image'], 255, method, type, na, c)

  kwargs['image'] = thrsh

  return kwargs
