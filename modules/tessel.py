
'''
Tessel operations
'''

from typing import Dict
import cv2
import numpy as np

def square(params: Dict, **data: Dict) -> Dict:
  '''
  Define tessel for an image from the image center

  Parameters:
    - params:
      cx: int=0; x coord center of the image
      cy: int=0; y coord center of the image
      size: List[int](5,7,9,11,13,17,19,21)=21; size of square's side
      colls: Scale[int](1,90,2,0)=10; number of collumns
      rows: Scale[int](3,90,2,0)=10; number of rows
      coll: Scale[int](0,89,1,0)=9; output collumn number
      row: Scale[int](0,89,1,0)=9; output row number
      offx: Scale[int](-10,10, 1, 0)=0; offset x
      offy: Scale[int](-10,10, 1, 0)=0; offset y
      show: bool=False; show the tessel 
    - data: 
      image: ndarray; the image
  Returns:
    - data:
      image: ndarray; the image
      outcoll: ndarray; the row of the tessel
      outrow: ndarray; the row of the tessel
      out: ndarray; the tessel image
      tessel: Dict; tessel for the image
  '''  

  cx = params.get('cx', 0)
  cy = params.get('cy', 0)
  size = params.get('size', 21)
  colls = params.get('colls', 10)
  rows = params.get('rows', 10)
  coll = params.get('coll', 9)
  row = params.get('row', 9)
  offy = params.get('offy', 0)
  offx = params.get('offx', 0)
  show = params.get('show', False)

  image = data.get('image')
  h, w = image.shape[:2]

  if cx < colls*size+offx:
    cx = w//2
  if cy < rows*size+offy:
    cy = h//2
  sx = cx + offx
  sy = cy + offy
  half = (size-1)//2

  before_cx = [i for i in range(sx-half-1, sx-half-colls*size//2, -size) if i > 0]
  after_cx = [i for i in range(sx+half, sx+half+colls*size//2, size) if i < w]
  cls = [*list(reversed(before_cx)), *after_cx]

  before_cy = [i for i in range(sy-half-1, sy-half-rows*size//2, -size) if i > 0]
  after_cy = [i for i in range(sy+half, sy+half+rows*size//2, size) if i < h]
  rls = [*list(reversed(before_cy)), *after_cy]
  tessel = {'cX': cx, 'cY':cy, 'coll':coll, 'row': row, 'size': size, 'colls': colls, 'rows': rows, 'X': cls, 'Y:': rls}

  outy = min(row, len(rls)-2)
  outx = min(coll, len(cls)-2)
  y0 = rls[outy]
  y1 = y0+size
  x0 = cls[outx]
  x1 = x0+size
  out = image[y0:y1, x0:x1]
  outcoll = image[rls[0]:rls[len(rls)-1], x0:x1]
  outrow = image[y0:y1, cls[0]:cls[len(cls)-1]]

  if show:
    color = (255,255,255)
    thickness = 1
    # Center of the image
    cv2.line(image, (cx,0), (cx,h), color=color, thickness=thickness)
    cv2.line(image, (0,cy), (w,cy), color=color, thickness=thickness)
    # Grid
    for c in cls:
      cv2.line(image, (c,rls[0]), (c,rls[-1]), color=color, thickness=thickness)
    for r in rls:
      cv2.line(image, (cls[0],r), (cls[-1],r), color=color, thickness=thickness)
    # Left, right side
    cv2.rectangle(image, (x0, y0), (x1, y1), color=color, thickness=thickness+2)

  data['out'] = out
  data['outcoll'] = outcoll
  data['outrow'] = outrow
  data['tessel'] = tessel
  return data

def _gcd(a: int, b: int) -> int:
  '''
  Calculate the Greatest Common Divisor of a and b.
  '''

  if a%b == 0:
      return b
  return _gcd(b, a%b)    