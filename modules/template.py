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
      image: ndarray; the image
      coords: Tuple[int]; coordinates of the bounding box - x0, y0, x1, y1
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
  coords = (top_left[0], top_left[1], bottom_right[0], bottom_right[1])

  data['coords'] = coords
  return data
