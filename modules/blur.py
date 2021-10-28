'''
Bluring operation
'''

import cv2
from typing import Dict


def avrg(params: Dict , **data: Dict) -> Dict:
  '''
  Average bluring.

  Parameters:
    - params keys:   
      kernel: List[int](3,5,7,9)=3; kernel size
    - data keys: 
      image: str ; the image
  Returns:
    - data keys:
      image: str ; the blured image
  '''

  kernel = params.get('kernel', 3)
  kX = kY = kernel 
  data['image'] = cv2.blur(data.get('image'), (kX, kY)) 
  return data
