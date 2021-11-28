'''
Scale, sample operations.
'''

from typing import Dict
import cv2


def sc_down(params: Dict , **data: Dict) -> Dict:
  '''
  Downscales an image

    Parameters:
    - params:   
      border: Dict[str,int](DEFAULT:4,REFLECT:2,REFLECT101:4,REFLECT_101:4,REPLICATE:1,TRANSPARENT:5,WRAP:3)=DEFAULT; pixel extrapolation method cv2.BORDER_(...)
    - data: 
      image: np.dtype; the image
  Returns:
    - data:
      image: np.dtype; the image
  '''

  border_type = params.get('border-type',cv2.BORDER_DEFAULT) # Pixel extrapolation method

  image = data.get('image')
  # By default, size of the output image is computed as Size((src.cols+1)/2, (src.rows+1)/2)

  data['n_layer_down'] = cv2.pyrDown(image, borderType=border_type) 
  return data

def sc_up(params: Dict , **data: Dict) -> Dict:
  '''
  Upscales an image

    Parameters:
    - params:   
      border: Dict[str,int](DEFAULT:4,REFLECT:2,REFLECT101:4,REFLECT_101:4,REPLICATE:1,TRANSPARENT:5,WRAP:3)=DEFAULT; pixel extrapolation method cv2.BORDER_(...)
    - data: 
      image: np.dtype; the image
  Returns:
    - data:
      image: np.dtype; the image
  '''

  border_type = params.get('border-type',cv2.BORDER_DEFAULT) # Pixel extrapolation method

  image = data.get('image')
  # By default, size of the output image is computed as Size((src.cols+1)/2, (src.rows+1)/2)

  data['n_layer_up'] = cv2.pyrUp(image, borderType=border_type) 
  return data

def sc_pyramid(params: Dict , **data: Dict) -> Dict:
  '''
  Downscales an image using  a gaussian pyramids

    Parameters:
    - params:
      level: int=1; pyramid level
      border: Dict[str,int](DEFAULT:4,REFLECT:2,REFLECT101:4,REFLECT_101:4,REPLICATE:1,TRANSPARENT:5,WRAP:3)=DEFAULT; pixel extrapolation method cv2.BORDER_(...)
    - data: 
      image: np.dtype; the image
  Returns:
    - data:
      pyramid: List[np.dtype]; the image pyramid
  '''
  level = params.get('level', 1)
  border_type = params.get('border-type',cv2.BORDER_DEFAULT) # Pixel extrapolation method

  image = data.get('image')

  pyramid = [image]
  for i in range(level):
    pyramid.append(cv2.pyrDown(pyramid[i-1], borderType=border_type))

  data['pyramid'] = pyramid
  return data