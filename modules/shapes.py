'''
Simple shapes generation operations
'''

import cv2
import numpy as np


def cnt_zero(step, **kwargs):
  '''
  Counts zeros in an binary image.

  Keyword arguments:
  - image: an binary image;

  Step arguments (--Type:Domain:[Possible Values]:Default-- name: description):
 
  Returns:
  - image: image;
  - zeros: number of zeros in the binary image;
  - equ: zeros == size
  '''  

  image = kwargs.get('image')
  size = np.size(image)

  zeros = size - cv2.countNonZero(image) 
  kwargs['zeros'] = zeros
  kwargs['equ'] = size == zeros
  
  return kwargs


def mask(step, **kwargs):
  '''
  Creats an empty mask
  Masking allows to focus only on parts of an image that interest us.
  A mask is the same size as our image, but has only two pixel values,
  0 and 255. Pixels with a value of 0 are ignored in the orignal image,
  and mask pixels with a value of 255 are allowed to be kept.

  Keyword arguments:
  - image: an image;

  Step arguments (--Type:Domain:[Possible Values]:Default-- name: description):
  --n;d;[ignore:0,kept:1];ignore -- type: mask's purpose (ignore, kept)
  --n;s;[];1-- idfact: increase/decrease factor
  --n;d;[rectangle:0,circle:1];rectangle-- area: opposite area on the mask(rectangle, circle)
  --n;s;[];0-- y0: left top coordinate of a rectangle area
  --n;s;[];h-- y1: left bottom coordinate of a rectangle area
  --n;s;[];0-- x0: left top coordinate of a rectangle area
  --n;s;[];w-- x1: right top coordinate of a rectangle area
  --n;s;[];w/2-- cx: center X coordinate of a circle area
  --n;s;[];h/2-- cy: a center Y coordinate of a circle area
  --n;s;[];min(h/2,w/2)-- rad: radius of a circle area

  Returns:
  - image: result image;
  - mask: mask
  '''  

  (h, w) = kwargs['image'].shape[:2]

  type = step.get('type', 0)
  idfact = step.get('idfact', 1)

  area = step.get('area', 0) 
  y0 = step.get('y0', 0)
  y1 = step.get('y1', h)
  x0 = step.get('x0', 0)
  x1 = step.get('x1', w)
  cx = step.get('cx', w / 2)
  cy = step.get('cy', h / 2)
  rad = step.get('rad', min(h / 2, w /2))
  
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
    cv2.circle(mask, (cx, cy), rad, value, -1)
 
  kwargs['mask'] = mask

  return kwargs


def shp_rectangle(step, **kwargs):
  '''
  Generates a white rectangle on a black background

  Keyword arguments:
  - image: an image;

  Step arguments (--Type;Domain;[Possible Values];Default-- name: description):
  --n;s;[];300-- h: an image height
  --n;s;[];300-- w: an image width
  --n;s;[];25-- tlx: x coordinate of the top left corner of rectangle
  --n;s;[];25-- tly: y coordinate of the top left corner of rectangle
  --n;s;[];275-- brx: x coordinate of the bottom right corner of rectangle
  --n;s;[];275-- bry: y coordinate of the bottom right corner of rectangle
  --s;l;['image', 'shape', 'mask'];'image'-- dst-key: destination key name

  Returns:
  - image: a black rectangle image;
  '''

  h = step.get('h', 300)
  w = step.get('w', 300)

  tlx = step.get('tlx', 25)
  tly = step.get('tly', 25)
  brx = step.get('brx', 275)
  bry = step.get('bry', 275)

  dst_key = step.get('dst-key', 'image')


  rectangle = np.zeros((h, w), dtype = "uint8")
  cv2.rectangle(rectangle, (tlx, tly), (brx, bry), 255, -1)

  kwargs[dst_key] = rectangle
   
  return kwargs


def shp_circle(step, **kwargs):
  '''
  Generates a white circle on a black background

  Keyword arguments:
  - image: an image;

  Step arguments (--Type;Domain;[Possible Values];Default-- name: description):
  --n;s;[];300-- h: an image height
  --n;s;[];300-- w: an image width
  --n;s;[];150-- cx: x coordinate of the center of an image
  --n;s;[];150-- cy: y coordinate of the center of an image
  --n;s;[];250-- r: a circle radius
  --s;l;['image', 'shape', 'mask'];'image'-- dst-key: destination key name

  Returns:
  - image: a black circle image;
  '''

  h = step.get('h', 300)
  w = step.get('w', 300)
  cx = step.get('cx', 150)
  cy = step.get('cy', 150)
  r = step.get('r', 150)

  dst_key = step.get('dst-key', 'image')

  circle = np.zeros((h, w), dtype = "uint8")
  cv2.circle(circle, (cx, cy), r, 255, -1)

  kwargs[dst_key] = circle
   
  return kwargs
