'''
Color spaces operations
'''

import cv2
from typing import Dict


def bgrto(params: Dict , **data: Dict) -> Dict:  
  '''
  Converts a colored (BGR) image to another color space.

  Parameters:
    - params:   
      type: Dict[str,int](BGR2BGRA:0,BGR2RGB:4,BGR2GRAY:6,BGR2XYZ:32,BGR2YCrCb:36,BGR2HSV:40,BGR2LAB:44,BGR2Luv:50,BGR2HLS:52,BGR2YUV:82)=BGR2GRAY; new color space, one from cv2.COLOR_(...)
    - data: 
      image: np.dtype; the image
  Returns:
    - data keys:
      image: np.dtype; the image in a new color space
'''  

  type = params.get('type', cv2.COLOR_BGR2GRAY)
  image = data.get('image')
  
  if len(image.shape) < 3:
    # input - gray or binary
    return data
  
  data['image'] = cv2.cvtColor(image, type)
  return data
