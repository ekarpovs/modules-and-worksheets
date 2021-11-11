'''
Basic operations
'''

from typing import Dict


def crop(params: Dict , **data: Dict) -> Dict:
  '''
  Crops an image.

  Parameters:
    - params:   
      y0: int=0; left top coordinate
      y1: int=100; left bottom coordinate
      x0: int=0; left top coordinate
      x1: int=100; right top coordinate
    - data: 
      image: np.dtype; the image
  Returns:
    - data keys:
      image: np.dtype; the result image
  '''  


  image = data.get('image')
  (h, w) = image.shape[:2]

  y0 = params.get('y0', 0)
  y1 = params.get('y1', 100)
  x0 = params.get('x0', 0)
  x1 = params.get('x1', 100)

  data['image'] = image[y0:y1, x0:x1]
  return data
