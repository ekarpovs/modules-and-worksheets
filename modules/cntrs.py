'''
Contours operations
'''
import cv2


def find(step, **kwargs):
  '''
  Finds contours of an image.

  Keyword arguments:
  - image: an image;

  Step arguments (key, default):
  - mth: approximation method, 2:
    - cv2.CHAIN_APPROX_NONE: 1
    - cv2.CHAIN_APPROX_SIMPLE: 2
    - cv2.CHAIN_APPROX_TC89_L1: 3
    - cv2.CHAIN_APPROX_TC89_KCOS: 4
  - md: result mode, 0:
    - cv2.RETR_EXTERNAL: 0
    - cv2.RETR_LIST: 1
    - cv2.RETR_CCOMP: 2
    - cv2.RETR_TREE: 3
    - cv2.RETR_FLOODFILL: 4
  
  Returns:
  - image;
  - cntrs: list of the contours.
  '''  

  mode = step.get('md', cv2.RETR_EXTERNAL)
  method = step.get('mth', cv2.CHAIN_APPROX_SIMPLE)

  cntrs = cv2.findContours(kwargs['image'], mode, method) 
  
  if len(cntrs) == 3:
      cntrs = cntrs[1]

  kwargs['cntrs'] = cntrs
  
  return kwargs



def sort(step, **kwargs):
  '''
  Sorts contours.

  Keyword arguments:
  - image: an image;
  - cntrs: contours;
 
   Step arguments (key, default):
   - rev: reverse flag, False;

  Returns:
  - image;
  - cntrs: list of the sorted contours.
  '''

  reverse = step.get('rev', True)

  cntrs = kwargs['cntrs']
 
  i = 0
  # construct the list of bounding boxes and sort them from top to
  # bottom
  bounding_boxes = [cv2.boundingRect(c) for c in cntrs]

  (cntrs, bounding_boxes) = zip(*sorted(zip(cntrs, bounding_boxes), key=lambda b:b[1][i], reverse=reverse))

  kwargs['cntrs'] = cntrs
  kwargs['boxes'] = bounding_boxes

  return kwargs



def sel_rect(step, **kwargs):
  '''
  Sorts contours.

  Keyword arguments:
  - image: an image;
  - cntrs: sorted contours;

  Returns:
  - image;
  - rect: the biggest rectangle contour.
  '''

  cntrs = kwargs['cntrs']
 
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

  kwargs['rect'] = rect

  return kwargs

