'''
Threshold operations
'''
from typing import Dict
import cv2


def simple(params: Dict , **data: Dict) -> Dict:
  '''
  Applies a fixed-level (or optimal) threshold to each array element.

  Parameters:
    - params:
      type: Dict[str,int](BINARY:0,BINARY_INV:1,TRUNC:2,TOZERO:3,TOZERO_INV:4)=BINARY; thresholding type cv2.THRES_(..)
      thrsh: Scale[int](0,255,1,0)=127; threshold
      otsu: bool=False; flag to use Otsu algorithm to choose the optimal threshold value
    - data: 
      image: array[dtype[uint8]]; an image
  Returns:
    - data:
      image: array[dtype[uint8]]; the result image
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


def adaptive(params: Dict , **data: Dict) -> Dict:
  '''
  Applies a fixed-level (or optimal) threshold to each array element.

  Parameters:
    - params:
      type: Dict[str,int](BINARY:0,BINARY_INV:1)=BINARY; thresholding type cv2.THRES_(..)
      max: Scale[int](225,255,1,0)=235; max threshhold
      meth: Dict[str,int](MEAN_C:0,GAUSSIAN_C:1)=MEAN_C; adaptive thresholding algorithm to use cv2.ADAPTIVE_THRESH_(...)
      na: Scale[int](3,21,1,1)=15; neighborhood area
      c: float=5.0; a constant which is subtracted from the mean or weighted mean calculated
    - data: 
      image: array[dtype[uint8]]; an image
  Returns:
    - data:
      image: array[dtype[uint8]]; the result image
'''

  type = params.get('type', cv2.THRESH_BINARY) 
  max = params.get('max',235) 
  method = params.get('meth', cv2.ADAPTIVE_THRESH_MEAN_C) 
  na = params.get('na',15) # neighborhood area
  c = params.get('c', 5) #  
  thrsh = cv2.adaptiveThreshold(data.get('image'), max, method, type, na, c)
  data['image'] = thrsh
  return data
