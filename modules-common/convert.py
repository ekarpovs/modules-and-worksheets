'''
Converts different formats
'''

import cv2
import numpy as np
from PIL import Image


def pil_to_cv2(params, **data):
  '''
  Converts image from PIL to cv2
  parameters:
    - params:
    - data: 
        image-pil - reference to an source image in PIL format
    returns:
      - data:
        - image: image in cv2 format.
  '''
  image_pil = data.get('image-pil')
  # image = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)
  image = np.asarray(image_pil, dtype=np.int64)
  data['image'] = image
  return data

def cv2_to_pil(params, **data):
  '''
  Converts image from cv2 to PIL
  parameters:
    - params:
    - data: 
        image-pil - reference to an source image in PIL format
    returns:
      - data:
        - image: image in cv2 format.
  '''
  # Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
  data['image-pil'] = Image.fromarray(data.get('image'))
  return data
