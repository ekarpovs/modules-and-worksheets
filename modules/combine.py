'''
Combine operations
  concat: Concatinates two images
'''

from typing import Dict
import cv2
import numpy as np


def concat(params: Dict , **data: Dict) -> Dict:
  '''
  Concatenates two images. Images have to have the same dimention.
  Parameters:
    - params:
    dsize: Scale[int](1,10,1,0)=5; delimeter size 
    - data: 
      image: ndarray; the first image
      image1: ndarray; the second image
  Returns:
    - data:
      image: ndarray; the new images
  '''
 
  d_size = params.get('dsize', 5)

  image= data.get('image')
  image1= data.get('image1')
  shape = image.shape
  shape_len = len(shape) 

  # create iamge stack and place to it the original image
  if shape_len >= 3:
    h, w, c = shape
    new_image = np.ones([h, w*2+d_size, c])*255
    new_image[:, :w, :] = image
    new_image[:, w+d_size:w*2+d_size, :] = image1
  else:
    h, w = shape
    new_image = np.ones([h, w*2+d_size])*255
    new_image[:, :w] = image
    new_image[:, w+d_size:w*2+d_size] = image1

  # convert dtype from float64 to uint8
  new_image = cv2.normalize(src=new_image, dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

  data['image'] = new_image
  return data
