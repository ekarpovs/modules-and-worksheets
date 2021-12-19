'''
Contours operations
'''
from typing import Dict
import cv2


def find(params: Dict , **data: Dict) -> Dict:
  '''
  Finds contours of an image.

  Parameters:
    - params:   
      meth: Dict[str,int](NONE:1,SIMPLE:2,TC89_L1:3,TC89_KCOS:4)=SIMPLE; interpolation method cv2.CHAIN_APPROX_(...)
      mode: Dict[str,int](EXTERNAL:0,LIST:1,CCOMP:2,TREE:3,FLOODFILL:4)=EXTERNAL; result mode cv2.RETR_(...)
      num-cntrs: int=5; number of biggets contours
      approx: bool=True; approximate as rectangle
    - data: 
      image: array[dtype[uint8]]; the image
  Returns:
    - data:
      cntrs: List[np.ndarray]; founded contours
  '''  

  mode = params.get('mode', cv2.RETR_EXTERNAL)
  method = params.get('meth', cv2.CHAIN_APPROX_SIMPLE)
  num_cntrs = params.get('num-cntrs', 5)
  
  image = data.get('image')

  cntrs, _ = cv2.findContours(image, mode, method) 
  if len(cntrs) == 3:
    cntrs = cntrs[1]
  cntrs = sorted(cntrs, key = cv2.contourArea, reverse = True)[:num_cntrs]
  bounding_boxes = [cv2.boundingRect(c) for c in cntrs]

  data['cntrs'] = cntrs
  data['boxes'] = bounding_boxes

  return data


def sort(params: Dict , **data: Dict) -> Dict:
  '''
  Sorts contours.

  Parameters:
    - params:   
      rev: bool=True; reverse flag
      max-num: int=5; max number of returned contours
    - data: 
      cntrs: List[np.ndarray]; contours
  Returns:
    - data:
      cntrs: List[np.ndarray]; sorted contours
      boxes: List[Tuple[]]; coordinates of bounding boxes
  '''

  reverse = params.get('rev', True)
  cntrs = data.get('cntrs')
  max_num = params.get('max-num', 5)

  i = 0
  # construct the list of bounding boxes and sort them from top to
  # bottom
  bounding_boxes = [cv2.boundingRect(c) for c in cntrs]
  cntrs = sorted(cntrs, key=cv2.contourArea, reverse=True)
  # (cntrs, bounding_boxes) = zip(*sorted(zip(cntrs, bounding_boxes), key=lambda b:b[1][i], reverse=reverse))
  if len(cntrs) > max_num:
    cntrs = cntrs[:max_num]
    bounding_boxes = bounding_boxes[:max_num]
  data['cntrs'] = cntrs
  data['boxes'] = bounding_boxes
  return data


def sel_rect(params: Dict , **data: Dict) -> Dict:
  '''
  Selects rectangle contours.

  Parameters:
    - params:   
    - data: 
      cntrs: np.ndarray; sorted contours
  Returns:
    - data:
      app-rect: np.ndarray; the biggest rectangle contour
  '''

  cntrs = data.get('cntrs')
  
 	# loop over the contours 
  for c in cntrs:
		# approximate the contour
	  peri = cv2.arcLength(c, True)
	  approx = cv2.approxPolyDP(c, 0.02 * peri, True)
		# if our approximated contour has four points, then we
		# can assume that we have found our screen
	  if len(approx) == 4:
		  rect = approx
		  break 
  data['app-rect'] = rect
  return data

