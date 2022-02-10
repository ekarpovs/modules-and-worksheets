'''
Template matching operations.
'''

from typing import Dict
import cv2


def single(params: Dict , **data: Dict) -> Dict:
  '''
  Template single matching with metods:
    Squared Difference,
    Normalized Squared Difference,
    Cross Correlation,
    Normalized Cross-Correlation,
    Cosine Coefficient,
    Normalized Cosine Coefficient.

    Parameters:
    - params:   
      method: Dict[str, int](cv2.TM_SQDIFF:0,cv2.TM_SQDIFF_NORMED:1,cv2.TM_CCORR:2,cv2.TM_CCORR_NORMED:3,cv2.TM_CCOEFF:4,cv2.TM_CCOEFF_NORMED:5)=TM_CCORR_NORMED; metod 
    - data:
      image: ndarray; the image
      template: ndarray; the template
  Returns:
    - data:
      location: Dict[str, int]; coordinates of the bounding box - x0, y0, x1, y1
  '''

  image = data.get('image')
  template = data.get('template')
  ht, wt = template.shape[:2]

  method = params.get('method', cv2.TM_CCORR_NORMED)

  res = cv2.matchTemplate(image, template, method)
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
  if method == cv2.TM_SQDIFF or method == cv2.TM_SQDIFF_NORMED:
    top_left = min_loc
  else:
    top_left = max_loc
  bottom_right = (top_left[0] + wt, top_left[1] + ht)
  x0 = top_left[0]
  y0 = top_left[1]
  x1 = bottom_right[0]
  y1 = bottom_right[1]
  cx = x0+x1//2 
  cy = y0+y1//2 

  data['location'] = {'cx': cx, 'cy': cy, 'coords': {'x0': x0, 'y0': y0, 'x1':x1, 'y1': y1}}
  return data

def join(params: Dict, **data: Dict) -> Dict:
  '''
  Joins find tempalte results

  Parameters:
    - params:
    - data: 
      crd1: Dict[str,str]={}; 1-st coordinates set
      crd2: Dict[str,str]={}; 2-nd coordinates set
      crd3: Dict[str,str]={}; 3-d coordinates set
  Returns:
    - data:
      coords: Dict[str,str]; dictioanary of cmp results
  '''

  crd1 = data.get('crd1',{})
  crd2 = data.get('crd2',{})
  crd3 = data.get('crd3',{})
  coords = {'coords': {'crd1': crd1, 'crd2': crd2, 'crd3': crd3}}
  data['coords'] = coords
  return data
