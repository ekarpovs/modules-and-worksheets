'''
Contours operations
'''
import cv2


def find(step, **kwargs):
  '''
  Finds contours of an image.

  Keyword arguments:
  - image: an image;

  Step arguments (--Type:Domain:[Possible Values]:Default-- name: description):
  --n;d;[NONE:1,SIMPLE:2,TC89_L1:3,TC89_KCOS:4];SIMPLE-- meth: interpolation method cv2.CHAIN_APPROX_(...)
  --n;d;[EXTERNAL:0,LIST:1,CCOMP:2,TREE:3,FLOODFILL:4];EXTERNAL-- md: result mode cv2.RETR_(...)
  
  Returns:
  - image;
  - cntrs: list of the contours.
  '''  

  mode = step.get('md', cv2.RETR_EXTERNAL)
  method = step.get('meth', cv2.CHAIN_APPROX_SIMPLE)

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

  Step arguments (--Type:Domain:[Possible Values]:Default-- name: description):
  --b;f;[False,True];False-- rev: reverse flag

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

