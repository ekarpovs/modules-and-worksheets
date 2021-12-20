'''
Drawing Points, Lines, Contours, Bounding boxes, Keypoints, Matches operation, etc.
'''

from typing import Dict, List
import cv2
import numpy as np

COLORS = [(0,0,0), (255,255,255), (0,0,255), (0,128,0), (255,0,0),  (255,0,255),  (0,255,255), (255,255,0), (0,255,0)]


def point(params: Dict , **data: Dict) -> Dict:
  '''
  Draws point.

  Parameters:
    - params:
      y0: int=0; point coordinate
      x0: int=0; point coordinate
      color: Dict[str, int](BLACK:0,WHITE:1,RED:2,GREEN:3, BLUE:4,MAGENTA:5,CYAN:6,YELLOW:7,LIME:8)=BLACK; the point color
    - data: 
      image: array[dtype[uint8]]; an image
  Returns:
    - data:
      image: array[dtype[uint8]]; an image
  '''
  image = data.get('image')

  x0 = params.get('x0', 0)
  y0 = params.get('y0', 0)
  color = params.get('color', 4)
  point_color=COLORS[color]

  image = cv2.circle(image, (x0,y0), radius=0, color=point_color, thickness=-1)
  return data

def line(params: Dict , **data: Dict) -> Dict:
  '''
  Draws line.

  Parameters:
    - params:
      x0: int=0; start point coordinate
      y0: int=0; start point coordinate
      x1: int=0; end point coordinate
      y1: int=0; end point coordinate
      color: Dict[str, int](BLACK:0,WHITE:1,RED:2,GREEN:3, BLUE:4,MAGENTA:5,CYAN:6,YELLOW:7,LIME:8)=BLACK; the point color
      thickness: int=1; thickness of the line
    - data: 
      image: array[dtype[uint8]]; an image
  Returns:
    - data:
      image: array[dtype[uint8]]; an image
  '''
  image = data.get('image')

  x0 = params.get('x0', 0)
  y0 = params.get('y0', 0)
  x1 = params.get('x1', 0)
  y1 = params.get('y1', 0)
  thickness = params.get('thickness', 1)
  color = params.get('color', 4)
  line_color=COLORS[color]

  image = cv2.line(image, (x0,y0), (x1,y1), color=line_color, thickness=thickness)
  return data


def contours(params: Dict , **data: Dict) -> Dict:
  '''
  Draws contours.

  Parameters:
    - params:
      thickness: int=1; thickness of the rectangle border (-1 fill the rectangle)
      color: Dict[str, int](BLACK:0,WHITE:1,RED:2,GREEN:3, BLUE:4,MAGENTA:5,CYAN:6,YELLOW:7,LIME:8)=BLACK; the contour color
      ccolor: Dict[str, int](BLACK:0,WHITE:1,RED:2,GREEN:3, BLUE:4,MAGENTA:5,CYAN:6,YELLOW:7,LIME:8)=BLACK; the center of a contour color
      tcolor: Dict[str, int](BLACK:0,WHITE:1,RED:2,GREEN:3, BLUE:4,MAGENTA:5,CYAN:6,YELLOW:7,LIME:8)=BLACK; the text of a contour color
    - data: 
      image: array[dtype[uint8]]; an image
      cntrs: List[np.ndarray]; contours
  Returns:
    - data:
      image: array[dtype[uint8]]; an image
  '''

  image = data.get('image')
  cntrs = data.get('cntrs')

  thickness = params.get('thickness', 1)
  color = params.get('color', 4)
  ccolor = params.get('ccolor', 2)
  tcolor = params.get('ccolor', 7)
  draw_color=COLORS[color]
  center_color=COLORS[ccolor]
  text_color = COLORS[tcolor]

  # loop over the contours and draw them
  for (i, c) in enumerate(cntrs):
    # orig = draw_contour(image.copy(), c, i)   
    # compute the center of the contour area and draw a circle
    # representing the center
    M = cv2.moments(c)
    if M['m00'] == 0:
      break
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    # draw the center of the contour on the image
    cv2.circle(image, (cX, cY), 10, center_color, -1) 
    # compute the area and the perimeter of the contour
    # area = cv2.contourArea(c)
    # perimeter = cv2.arcLength(c, True)
    # print("Contour #{} -- area: {:.2f}, perimeter: {:.2f}".format(i + 1, area, perimeter))
    # draw the contour on the image
    image = cv2.drawContours(image, [c], -1, draw_color, thickness) 
    # draw the countour number on the image
    cv2.putText(image, "#{}".format(i + 1), (cX - 20, cY), cv2.FONT_HERSHEY_SIMPLEX,
      1.0, text_color, 2) 
  return data


def keypoints(params: Dict , **data: Dict) -> Dict:
  """
  Draws keypoints.

  Parameters:
    - params:
      flags: Dict[str, int](DEFAULT:0,DRAW_OVER_OUTIMG:1,NOT_DRAW_SINGLE_POINTS:2,DRAW_RICH_KEYPOINTS:4)=DRAW_RICH_KEYPOINTS; flags cv2.DRAW_MATCHES_FLAGS_(...)
      color: Dict[str, int](BLACK:0,WHITE:1,RED:2,GREEN:3, BLUE:4,MAGENTA:5,YELLOW:6,CYAN:7,LIME:8)=BLACK; keypoins color
    - data: 
      image: array[dtype[uint8]]; an image
      kpnts: List[KeyPoint]; blobs keypoints
  Returns:
    - data:
      image: array[dtype[uint8]]; an image with keypoints
  """

  flags = params.get('flags', cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
  color = params.get('color', 2)
  # RGB
  draw_color=COLORS[color]

  image = data.get('image')
  clone = image.copy()
  keypoints = data.get('kpnts')
  im_with_keypoints = np.array([])
  if flags == cv2.DRAW_MATCHES_FLAGS_DRAW_OVER_OUTIMG:
    im_with_keypoints = clone
  im_with_keypoints = cv2.drawKeypoints(clone, keypoints, im_with_keypoints, draw_color, flags)
  data['image'] = im_with_keypoints
  return data


# https://docs.opencv.org/3.4/d4/d5d/group__features2d__draw.html
def matches(params: Dict , **data: Dict) -> Dict:
  """
  Draws matches.

  Parameters:
    - params:
    - data: 
      image: array[dtype[uint8]]; an image
      image1: array[dtype[uint8]]; an image
      kpnts: np.ndarray; keypoints
      kpnts1: np.ndarray; keypoints
  Returns:
    - data:
      image: array[dtype[uint8]]; an image with matches
  """

  first = data.get('image')
  second = data.get('image1')
  kpnts1 = data.get('kpnts1')
  kpnts2 = data.get('kpnts2')
  matches1to2 = data.get('matches')

  matched_visual	=	cv2.drawMatches(first, kpnts1, second, kpnts2, matches1to2, None) 
  data['image'] = matched_visual
  return data

def box(params: Dict , **data: Dict) -> Dict:
  '''
  Draws bounding box.

  Parameters:
    - params:
      thickness: int=1; thickness of the rectangle border (-1 fill the rectangle)
      color: Dict[str, int](BLACK:0,WHITE:1,RED:2,GREEN:3, BLUE:4,MAGENTA:5,CYAN:6,YELLOW:7,LIME:8)=BLACK; the box color
    - data: 
      image: array[dtype[uint8]]; an image
      coord: List[int](x0,y0,x1,y1); coordinates
  Returns:
    - data:
      image: array[dtype[uint8]]; an image
  '''

  image = data.get('image')
  clone = image.copy()
  coords = data.get('coords')

  thickness = params.get('thickness', 1)
  color = params.get('color', 4)
  draw_color=COLORS[color]

  if thickness is not 0:
    x0,y0,x1,y1 = coords
    cv2.rectangle(clone, (x0, y0), (x1, y1), draw_color, thickness)
  return data