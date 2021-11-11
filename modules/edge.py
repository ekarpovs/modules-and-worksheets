'''
Gradient and edge dectection operations
Gradient magnitude and orientation.
'''

from typing import Dict
import cv2
import numpy as np


def canny(params: Dict , **data: Dict) -> Dict:
  '''
  Computes a "wide", "mid-range", and "tight" threshold for the edges.

  Parameters:
    - params:   
      thrs1: Range[int](10,150,1)=50; threshold1
      thrs2: Range[int](100,252,1)=200; threshold2
    - data: 
      image: np.dtype; the image
  Returns:
    - data:
      image: np.dtype; the blured image
  '''

  threshold1 = params.get('thrs1', 10)
  threshold2 = params.get('thrs2', 200)
  data['image'] = cv2.Canny(data.get('image'), threshold1, threshold2)
  return data
