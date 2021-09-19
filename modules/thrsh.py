'''
Threshold operations
'''
import cv2


def simple(params, **data):
  '''
  Applies a fixed-level (or optimal) threshold to each array element.

  parameters:
    - params: 
      --n;d;[BINARY:0,BINARY_INV:1,TRUNC:2,TOZERO:3,TOZERO_INV:4];BINARY-- type: thresholding type cv2.THRES_(..)
      --n;r;[0,255];127-- thrsh: threshold value
      --b;f;[False,True];False-- otsu:  flag to use Otsu algorithm to choose the optimal threshold value
    - data: 
        image - reference to the image
  returns:
    - data: 
        image - reference to the result binary image
  '''
  type = params.get('type', cv2.THRESH_BINARY)
  threshold = params.get('thrsh', 127)
  max_val = params.get('max-val', 255)
  otsu = params.get('otsu', False)
  if otsu:
    type |= cv2.THRESH_OTSU
    threshold = 0
  (T, thrsh) = cv2.threshold(data.get('image'), threshold, max_val, type)
  data['image'] = thrsh
  return data


def adaptive(params, **data):
  '''
  Applies a fixed-level (or optimal) threshold to each array element.

  parameters:
    - params: 
      --n;d;[BINARY:0,BINARY_INV:1,TRUNC:2,TOZERO:3,TOZERO_INV:4];BINARY-- type: thresholding type cv2.THRES_(...)
      --n;d;[MEAN_C:0,GAUSSIAN_C:1];MEAN_C-- meth: adaptive thresholding algorithm to use cv2.ADAPTIVE_THRESH_(...)
      --n;s;[];15-- na: neighborhood area
      --n;s;[];5-- c: a constant which is subtracted from the mean or weighted mean calculated
    - data: 
        image - reference to the image
  returns:
    - data: 
        image - reference to the result binary image
'''
  type = params.get('type', cv2.THRESH_BINARY) 
  method = params.get('meth', cv2.ADAPTIVE_THRESH_MEAN_C) 
  na = params.get('na',15) # neighborhood area
  c = params.get('c', 5) #  
  thrsh = cv2.adaptiveThreshold(data.get('image'), 255, method, type, na, c)
  data['image'] = thrsh
  return data
