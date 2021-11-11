'''
Simple shapes generation operations
'''

from re import L
import cv2
import numpy as np


def mask(params, **data):
  '''
  Creats an empty mask
  Masking allows to focus only on parts of an image that interest us.
  A mask is the same size as our image, but has only two pixel values,
  0 and 255. Pixels with a value of 0 are ignored in the orignal image,
  and mask pixels with a value of 255 are allowed to be kept.

    Parameters:
    - params:   
      type: Dict[str,int](ignore:0,kept:1)=ignore; mask's purpose ignore(black) , kept(white)
      idfact: float=1.0; increase/decrease factor
      h: int=300; an image height
      w: int=300; an image width
      area: Dict[str,int](rectangle:0,circle:1)=rectangle; opposite area on the mask(rectangle, circle)
      y0: int=0; left top coordinate of a rectangle area
      y1: int=300; left bottom coordinate of a rectangle area
      x0: int=0; left top coordinate of a rectangle area
      x1: int=300; right top coordinate of a rectangle area
      cx: int=150; x coordinate of the center of an image
      cy: int=150; y coordinate of the center of an image
      r: int=150; the circle radius
    - data: 
  Returns:
    - data:
      mask: np.dtype; the mask
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
  data['mask'] = mask
  return data
