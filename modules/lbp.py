'''
Local binary patterns descriptors
'''

import cv2
from skimage import feature
from typing import Dict


def lbp(params: Dict , **data: Dict) -> Dict:
  '''
  Computes LBP representation of an image.

  Parameters:
    - params:   
      points: List[int](8,16,24,32,40,48,56)=8; number of points in the LBP
      radius: Scale[int](1,7,1,0)=1; radius of the LBP
    - data: 
      image: array[dtype[uint8]]; the image
  Returns:
    - data:
      lbp: array[dtype[float64]];
  '''

  num_points = params.get('points', 8)
  radius = params.get('radius', 1)

  image = data.get('image')

  lbp = feature.local_binary_pattern(image, num_points, radius, method="uniform")

  data['lbp'] = lbp
  return data
