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
      ap-size: Scale[int](1,7,1,1)=3; aperture size
      thrs1: Scale[int](10,150,1,0)=50; threshold1
      thrs2: Scale[int](100,252,1,0)=200; threshold2
    - data: 
      image: array[dtype[uint8]]; the image
  Returns:
    - data:
      image: array[dtype[uint8]]; the result image
  '''

  threshold1 = params.get('thrs1', 50)
  threshold2 = params.get('thrs2', 200)
  ap_size = params.get('ap-size', 3)

  image = data.get('image')

  data['image'] = cv2.Canny(image, threshold1, threshold2, apertureSize=ap_size)
  return data

def laplacian(params: Dict , **data: Dict) -> Dict:
  '''
  Computes the Laplacian of the image .

  Parameters:
    - params:   
      kernel: Scale[int](1,7,1,1)=3; kernel size
    - data: 
      image: array[dtype[uint8]]; the image
  Returns:
    - data:
      image: array[dtype[uint8]]; the result image
  '''

  kernel = params.get('kernel', 3)
  image = data.get('image')

  lap = cv2.Laplacian(image, cv2.CV_64F, ksize=kernel)
  data['image'] = np.uint8(np.absolute(lap)) 
  return data

def sobel(params: Dict , **data: Dict) -> Dict:
  '''
  Computes gradients along the X or Y axis uses Sobel algorithm.

  Parameters:
    - params:   
      kernel: Scale[int](1,7,1,1)=3; kernel size
      direction: Dict[str,int](horizontal:0,vertical:1)=horizontal; direction (x, y)
      convert: bool=True; convert result to unsigned 8-bit integer representation
    - data: 
      image: array[dtype[uint8]]; the image
  Returns:
    - data:
      image: array[dtype[uint8]]; the result image
  '''

  kernel = params.get('kernel', 3)
  convert = params.get('convert', True)
  direction = params.get('direction', 0)
  image = data.get('image') 

  dx = 1
  dy = 0
  if direction == 1:
    dx = 0
    dy = 1
  # compute gradients along the X or Y axis
  grad = cv2.Sobel(image, ddepth=cv2.CV_64F, dx=dx, dy=dy, ksize=kernel) 
  # images are now of the floating point data type,
  # so convert them back a to unsigned 8-bit integer representation
  if convert:
    grad = cv2.convertScaleAbs(grad)
  data['image'] = grad
  return data

def within_bound(params: Dict , **data: Dict) -> Dict:
  '''
  Computes the gradient magnitude and orientation.
  Find all pixels that are within the upper and low angle boundaries

  Parameters:
    - params: 
      lower: Scale[float](150.0,180.0,1.0, 0)=175.0; lower orientation angle
      upper: Scale[float](150.0,180.0,1.0, 0)=180.0; upper orientation angle
    - data:
      gray: array[dtype[uint8]]; gray image, that was passed to Sobel
      image-gx: array[dtype[uint8]]; the first image
      image-gy: array[dtype[uint8]]; the second image
  Returns:
    - data:
      mask: array[dtype[uint8]]; pixels that are within
  '''

  lower = params.get('lower', 175)
  upper = params.get('upper', 180)

  gray = data.get('gray') 
  image_gx = data.get('image-gx') 
  image_gy = data.get('image-gy') 

  # compute the gradient magnitude and orientation, respectively
  mag = np.sqrt((image_gx ** 2) + (image_gy ** 2))
  orientation = np.arctan2(image_gy, image_gx) * (180 / np.pi) % 180
  # find all pixels that are within the upper and low angle boundaries
  idxs = np.where(orientation >= lower, orientation, -1)
  idxs = np.where(orientation <= upper, idxs, -1)
  mask = np.zeros(gray.shape, dtype="uint8")
  mask[idxs > -1] = 255 

  # data['mag'] = mag
  data['mask'] = mask
  return data



#scharr
#norm_factor = 32
#gradx = cv2.Scharr(img, cv2.CV_32F, 1, 0, scale=1.0/norm_factor)
#grady = cv2.Scharr(img, cv2.CV_32F, 0, 1, scale=1.0/norm_factor)


#prewitt
#kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
#kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
#img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
#img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)