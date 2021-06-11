'''
Simple shape generation operation
'''
import cv2
import numpy as np


def shp_rectangle(step, **kwargs):
  '''
  Generate a white rectangle on a black background

  Keyword arguments:
  - image: an image;

  Step arguments (--Type;Domain;[Possible Values];Default-- name: description):
  --n;s;[];300-- h: an image height
  --n;s;[];300-- w: an image width
  --n;s;[];25-- tlx: x coordinate of the top left corner of rectangle
  --n;s;[];25-- tly: y coordinate of the top left corner of rectangle
  --n;s;[];275-- brx: x coordinate of the bottom right corner of rectangle
  --n;s;[];275-- bry: y coordinate of the bottom right corner of rectangle
  
  Returns:
  - image: a black rectangle image;
  '''

  h = step.get('h', 300)
  w = step.get('w', 300)

  tlx = step.get('tlx', 25)
  tly = step.get('tly', 25)
  brx = step.get('brx', 275)
  bry = step.get('bry', 275)


  rectangle = np.zeros((h, w), dtype = "uint8")
  cv2.rectangle(rectangle, (tlx, tly), (brx, bry), 255, -1)

  kwargs['image'] = rectangle
   
  return kwargs


def shp_circle(step, **kwargs):
  '''
  Generate a white circle on a black background

  Keyword arguments:
  - image: an image;

  Step arguments (--Type;Domain;[Possible Values];Default-- name: description):
  --n;s;[];300-- h: an image height
  --n;s;[];300-- w: an image width
  --n;s;[];150-- cx: x coordinate of the center of an image
  --n;s;[];150-- cy: y coordinate of the center of an image
  --n;s;[];250-- r: a circle radius

  Returns:
  - image: a black circle image;
  '''

  h = step.get('h', 300)
  w = step.get('w', 300)
  cx = step.get('cx', 150)
  cy = step.get('cy', 150)
  r = step.get('r', 150)

  circle = np.zeros((h, w), dtype = "uint8")
  cv2.circle(circle, (cx, cy), r, 255, -1)

  kwargs['image'] = circle
   
  return kwargs



# a circle
circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
