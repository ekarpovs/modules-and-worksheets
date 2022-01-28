
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
      size: List[int](5,7,9,11)=11; size of square's side
      cells: Scale[int](1,30,2,0)=9; number of cells
      rows: Scale[int](3,30,2,0)=9; number of rows
      offx: Scale[int](-5,5, 1, 0)=0; offset x
      offy: Scale[int](-5,5, 1, 0)=0; offset y
      show: bool=False; show the tessel 
    - data: 
      image: ndarray; the image
  Returns:
    - data:
      image: ndarray; the image
      tessel: Dict; tessel for the image
  '''  

  size = params.get('size', 11)
  rows = params.get('rows', 10)
  cells = params.get('cells', 10)
  offx = params.get('offx', 0)
  offy = params.get('offy', 0)
  show = params.get('show', False)

  image = data.get('image')
  h, w = image.shape[:2]

  cx = w//2
  cy = h//2
  sx = cx + offx
  sy = cy + offy
  half = (size-1)//2

  before_cx = [i for i in range(sx-half-1, sx-half-cells*size//2, -size) if i > 0]
  after_cx = [i for i in range(sx+half, sx+half+cells*size//2, size) if i < w]
  cls = [*list(reversed(before_cx)), *after_cx]

  before_cy = [i for i in range(sy-half-1, sy-half-rows*size//2, -size) if i > 0]
  after_cy = [i for i in range(sy+half, sy+half+rows*size//2, size) if i < h]
  rls = [*list(reversed(before_cy)), *after_cy]
  tessel = {'cX': cx, 'cY':cy, 'size': size, 'cells': cells, 'rows': rows, 'X': cls, 'Y:': rls}

  if show:
    cv2.line(image, (cx,0), (cx,h), color=(255,255,255), thickness=1)
    cv2.line(image, (0,cy), (w,cy), color=(255,255,255), thickness=1)
    for c in cls:
      cv2.line(image, (c,rls[0]), (c,rls[-1]), color=(255,255,255), thickness=1)
    for r in rls:
      cv2.line(image, (cls[0],r), (cls[-1],r), color=(255,255,255), thickness=1)

  data['tessel'] = tessel
  return data

  def _gcd(a: int, b: int) -> int:
    '''
    Calculate the Greatest Common Divisor of a and b.
    '''

    if a%b == 0:
        return b
    return gcd(b, a%b)    