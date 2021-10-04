'''
Contours operations
'''
import cv2


def find(params, **data):
  '''
  Finds contours of an image.

  parameters:
    - params: 
      --n;d;[NONE:1,SIMPLE:2,TC89_L1:3,TC89_KCOS:4];SIMPLE-- meth: interpolation method cv2.CHAIN_APPROX_(...)
      --n;d;[EXTERNAL:0,LIST:1,CCOMP:2,TREE:3,FLOODFILL:4];EXTERNAL-- md: result mode cv2.RETR_(...)
    - data: 
        image - reference to the image 
  returns:
    - data: 
        cntrs - list of the founded contours
  '''  
  mode = params.get('md', cv2.RETR_EXTERNAL)
  method = params.get('meth', cv2.CHAIN_APPROX_SIMPLE)

  cntrs, _ = cv2.findContours(data.get('image'), mode, method) 
  if len(cntrs) == 3:
      cntrs = cntrs[1]
  data['cntrs'] = cntrs 
  return data


def sort(params, **data):
  '''
  Sorts contours.

  parameters:
    - params: 
      --b;f;[False,True];True-- rev: reverse flag
    - data: 
      cntrs - contours
  returns:
    - data: 
        cntrs - list of the sorted contours
        boxes - coordinates of bounding boxes
  '''
  reverse = params.get('rev', True)
  cntrs = data.get('cntrs')
  i = 0
  # construct the list of bounding boxes and sort them from top to
  # bottom
  # bounding_boxes = [cv2.boundingRect(c) for c in cntrs]
  # (cntrs, bounding_boxes) = zip(*sorted(zip(cntrs, bounding_boxes), key=lambda b:b[1][i], reverse=reverse))
  cntrs = sorted(cntrs, key=cv2.contourArea, reverse=True)


  data['cntrs'] = cntrs
  # data['boxes'] = bounding_boxes
  return data


def sel_rect(params, **data):
  '''
  Selects rectangle contours.

  parameters:
    - params: 
    - data: 
      cntrs - sorted contours 
  returns:
    - data: 
        rect - the biggest rectangle contour
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

