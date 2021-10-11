'''
Simple shapes generation operations
'''

from re import L
import cv2
import numpy as np

COLORS = [(0,0,0), (255,255,255), (255,0,0), (0,128,0), (0,0,255),  (255,0,255),  (0,255,255), (255,255,0), (0,255,0)]

def cnt_zero(params, **data):
  '''
  Counts zeros in an binary image.

  parameters:
    - params: 
    - data: 
        image - reference to the binary image
  returns:
    - data: 
      zeros - number of zeros in the binary image;
      equ - zeros == size
  '''  
  image = data.get('image')
  size = np.size(image)
  zeros = size - cv2.countNonZero(image) 
  data['zeros'] = zeros
  data['equ'] = size == zeros
  return data


def mask(params, **data):
  '''
  Creats an empty mask
  Masking allows to focus only on parts of an image that interest us.
  A mask is the same size as our image, but has only two pixel values,
  0 and 255. Pixels with a value of 0 are ignored in the orignal image,
  and mask pixels with a value of 255 are allowed to be kept.

  parameters:
    - params: 
      --n;d;[ignore:0,kept:1];ignore -- type: mask's purpose ignore(black) , kept(white))
      --n;s;[];1-- idfact: increase/decrease factor
      --n;s;[];300-- h: an image height
      --n;s;[];300-- w: an image width
      --n;d;[rectangle:0,circle:1];rectangle-- area: opposite area on the mask(rectangle, circle)
      --n;s;[];0-- y0: left top coordinate of a rectangle area
      --n;s;[];300-- y1: left bottom coordinate of a rectangle area
      --n;s;[];0-- x0: left top coordinate of a rectangle area
      --n;s;[];300-- x1: right top coordinate of a rectangle area
      --n;s;[];150-- cx: x coordinate of the center of an image
      --n;s;[];150-- cy: y coordinate of the center of an image
      --n;s;[];150-- r: a circle radius
      --s;l;[image, shape, mask];image-- dst-key: destination key name
    - data: 
        image - reference to the image
  returns:
    - data: 
      mask - mask
  '''  
  h = params.get('h', 300)
  w = params.get('w', 300)
  type = params.get('type', 0)
  idfact = params.get('idfact', 1)
  area = params.get('area', 0) 
  y0 = params.get('y0', 0)
  y1 = params.get('y1', 300)
  x0 = params.get('x0', 0)
  x1 = params.get('x1', 300)
  cx = params.get('cx', 150)
  cy = params.get('cy', 150)
  r = params.get('r', 150)
  dst_key = params.get('dst-key', 'image')

  if type == 0:
    # Create matrix (filled with zeros)
    mask = np.zeros((h,w), dtype="uint8")
    value = 255
  else:
    # Create matrix (filled with ones) and the multiplying it by 'ifact' to create an
    # array filled with ifact value's, then add the images together; 
    # the image will "brighter"
    mask = np.ones((h,w), dtype = "uint8") * idfact
    value = 0
  if area == 0:
    # Construct a rectangular area on the mask
    cv2.rectangle(mask, (x0, y0), (x1, y1), value, -1)
  else:
    # Construct a circular area on the mask
    cv2.circle(mask, (cx, cy), r, value, -1)
  data[dst_key] = mask
  return data


def shp_rectangle(params, **data):
  '''
  Generates a white rectangle on a black background

  parameters:
    - params: 
      --n;s;[];300-- h: an image height
      --n;s;[];300-- w: an image width
      --n;s;[];25-- tlx: x coordinate of the top left corner of rectangle
      --n;s;[];25-- tly: y coordinate of the top left corner of rectangle
      --n;s;[];275-- brx: x coordinate of the bottom right corner of rectangle
      --n;s;[];275-- bry: y coordinate of the bottom right corner of rectangle
      --n;s;[];1-- thickness: thickness of the rectangle border (-1 fill the rectangle)
      --n;d;[BLACK:0,WHITE:1,RED:2,GREEN:3, BLUE:4,MAGENTA:5,CYAN:6,YELLOW:7,LIME:8];WHITE-- color: shape color
      --s;l;[image, shape, mask];image-- dst-key: destination key name
    - data: 
        image - reference to the image
  returns:
    - data: 
        dst_key - reference to the black rectangle image
  '''
  h = params.get('h', 300)
  w = params.get('w', 300)

  tlx = params.get('tlx', 25)
  tly = params.get('tly', 25)
  brx = params.get('brx', 275)
  bry = params.get('bry', 275)
  thickness = params.get('thickness', 1)
  color = params.get('color', 1)
  dst_key = params.get('dst-key', 'image')
  
  shape_color=COLORS[color]
  canvas = np.ones((h, w, 3), dtype = "uint8")
  cv2.rectangle(canvas, (tlx, tly), (brx, bry), shape_color, thickness)
  data[dst_key] = canvas  
  return data


def shp_circle(params, **data):
  '''
  Generates a white circle on a black background

  parameters:
    - params: 
      --n;s;[];300-- h: an image height
      --n;s;[];300-- w: an image width
      --n;s;[];150-- cx: x coordinate of the center of an image
      --n;s;[];150-- cy: y coordinate of the center of an image
      --n;s;[];25-- r: a circle radius
      --n;s;[];1-- thickness: thickness of the circle border (-1 fill the circle)
      --n;d;[BLACK:0,WHITE:1,RED:2,GREEN:3, BLUE:4,MAGENTA:5,CYAN:6,YELLOW:7,LIME:8];WHITE-- color: shape color
      --s;l;[image, shape, mask];image-- dst-key: destination key name
    - data: 
        image - reference to the image
  returns:
    - data: 
        dst_key - reference to the black circle image
  '''
  h = params.get('h', 300)
  w = params.get('w', 300)
  cx = params.get('cx', 150)
  cy = params.get('cy', 150)
  r = params.get('r', 25)
  thickness = params.get('thickness', 1)
  color = params.get('color', 1)
  dst_key = params.get('dst-key', 'image')

  shape_color=COLORS[color]

  if r > h//2 or r > w//2:
    r = min(h//2, w//2)-1
  canvas = np.ones((h, w, 3), dtype = "uint8")
  cv2.circle(canvas, (cx, cy), r, shape_color, thickness)
  data[dst_key] = canvas  
  return data
