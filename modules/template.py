'''
Template matching operations.
'''

from typing import Dict
import cv2


def single(params: Dict , **data: Dict) -> Dict:
  '''
  Find template on an image

    Parameters:
    - params:   
      method: Dict[str, int](TM_CCORR_NORMED:0,TM_CCORR:1)=TM_CCORR_NORMED; metod 
    - data:
      image: np.dtype; the image
      template: np.dtype; the template
  Returns:
    - data:
      image: np.dtype; the image
      coords: Tuple[int](x0, y0, x1, y1); coordinates of the bounding box
  '''


  image = data.get('image')
  template = data.get('template')
  ht, wt = template.shape[:2]

  method = params.get('method', cv2.TM_CCORR_NORMED)

  res = cv2.matchTemplate(image, template, method)
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
  top_left = max_loc
  bottom_right = (top_left[0] + wt, top_left[1] + ht)
  coords = (top_left[0], top_left[1], bottom_right[0], bottom_right[1])
  
  data['coords'] = coords
  return data
