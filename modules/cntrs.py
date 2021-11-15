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
    - data: 
      image: np.dtype; the image
  Returns:
    - data:
      cntrs: List[int]; founded contours
  '''  

  mode = params.get('mode', cv2.RETR_EXTERNAL)
  method = params.get('meth', cv2.CHAIN_APPROX_SIMPLE)

  cntrs, _ = cv2.findContours(data.get('image'), mode, method) 
  if len(cntrs) == 3:
      cntrs = cntrs[1]
  data['cntrs'] = cntrs 
  return data


def sort(params: Dict , **data: Dict) -> Dict:
  '''
  Sorts contours.

  Parameters:
    - params:   
      rev: bool=True; reverse flag
    - data: 
      cntrs: List[]()=[]; contours
  Returns:
    - data:
      cntrs: List[]; sorted contours
      boxes: List[List[int]]; coordinates of bounding boxes
  '''

  reverse = params.get('rev', True)
  cntrs = data.get('cntrs')
  i = 0
  # construct the list of bounding boxes and sort them from top to
  # bottom
  bounding_boxes = [cv2.boundingRect(c) for c in cntrs]
  # cntrs = sorted(cntrs, key=cv2.contourArea, reverse=True)
  (cntrs, bounding_boxes) = zip(*sorted(zip(cntrs, bounding_boxes), key=lambda b:b[1][i], reverse=reverse))

  data['cntrs'] = cntrs
  data['boxes'] = bounding_boxes
  return data


def sel_rect(params: Dict , **data: Dict) -> Dict:
  '''
  Selects rectangle contours.

  Parameters:
    - params:   
    - data: 
      cntrs: List[]()=[]; sorted contours
  Returns:
    - data:
      rect: List[int]()=[]; the biggest rectangle contour
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
  data['rect'] = rect
  return data

