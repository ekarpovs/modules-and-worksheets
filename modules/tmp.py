'''
Temporary solutions - will decollated an implemented as worksheets
'''
from typing import Dict
import cv2
import numpy as np

def skeleton(params: Dict , **data: Dict) -> Dict:
  '''
  Creates binary image.

  Parameters:
    - params:
      type: Dict[str,int](BINARY:0,BINARY_INV:1,TRUNC:2,TOZERO:3,TOZERO_INV:4)=BINARY; thresholding type cv2.THRES_(..)
      thrsh: Scale[int](0,255,1,0)=75; threshold
      otsu: bool=False; flag to use Otsu algorithm to choose the optimal threshold value
      shape: Dict[str,int](RECT:0,CROSS:1,ELLIPSE:2)=CROSS; shape of structuring element cv2.MORPH_(...)
      kernel: Scale[int](3,13,1,1)=3; kernel size
    - data: 
      image: ndarray; an image
  Returns:
    - data:
      skeleton: ndarray; the result binary image
      shape: Dict[str, int]; the shape of the result image
  '''
  type = params.get('type', cv2.THRESH_BINARY)
  threshold = params.get('thrsh', 75)
  max_val = params.get('max-val', 255)
  otsu = params.get('otsu', False)
  shape = params.get('shape',cv2.MORPH_CROSS)
  kernel_size = params.get('kernel', 3)

  if otsu:
    type |= cv2.THRESH_OTSU
    threshold = 0

  image = data.get('image')

  size = np.size(image)
  skel = np.zeros(image.shape, np.uint8)

  (T, image) = cv2.threshold(image, threshold, max_val, type)

  elem = cv2.getStructuringElement(shape, ksize=(kernel_size, kernel_size))

  zeros = size
  done = False
  while( not done):
    eroded = cv2.erode(image, elem)
    temp = cv2.dilate(eroded, elem)
    temp = cv2.subtract(image, temp)
    skel = cv2.bitwise_or(skel, temp)
    image = eroded.copy()   
    zeros = size - cv2.countNonZero(image)   
    if zeros==size or zeros<=0:
        done = True

  (h, w) = skel.shape[:2]
  data['skeleton'] = skel
  data['shape'] = {'shape': {'h': h, 'w': w}}
  return data

