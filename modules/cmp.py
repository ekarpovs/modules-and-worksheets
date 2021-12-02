'''
Compare operations
'''

from typing import Dict
import cv2
import numpy as np
# from skimage.measure import compare_ssim
# from skimage.measure import structural_similarity as ssim
from math import log10, sqrt


def cmp_mse(params: Dict, **data: Dict) -> Dict:
  '''
  Calculates 'Mean Squared Error' between pixels of two images.
  The 'Mean Squared Error' between the two images is the
  sum of the squared difference between the two images.
  This two images must have the same dimension.

  Parameters:
    - params:
    - data: 
      image: np.dtype; the first image
      scene: np.dtype; the second image
  Returns:
    - data:
      mse: float; Mean Squared Errors
  '''  
  image = data.get('image')
  scene = data.get('scene')

  err = np.sum((image.astype("float") - scene.astype("float")) ** 2)
  err /= float(image.shape[0] * image.shape[1])
  # print('cmp_mse err:', err)
  data['mse'] = err
  return data


# def cmp_ssim(params: Dict, **data: Dict) -> Dict:
#   '''
#   Calculates 'Structural Similarity Index' between pixels of two images.
#   Uses to compare two windows instead an entire images.
#   This two images must have the same dimension.

#   Parameters:
#     - params:
#     - data: 
#       image: np.dtype; the first image
#       scene: np.dtype; the second image
#   Returns:
#     - data:
#       ssim: float; Structural Similarity Index
#   '''

#   image = data.get('image')
#   scene = data.get('scene')
#   s, diff = compare_ssim(image, scene, full=True, multichannel=True)
#   print('cmp_ssim s:', s)
#   data['ssim'] = s 
#   return data


def cmp_psnr(params: Dict, **data: Dict) -> Dict:
  '''
  Calculates 'Peak Signal-to-Noise Ratio' between two images.
  This two images must have the same dimension.

  Parameters:
    - params:
    - data: 
      image: np.dtype; the first image
      scene: np.dtype; the second image
  Returns:
    - data:
      psnr: float; Peak Signal-to-Noise Ratio
  '''  

  image = data.get('image')
  scene = data.get('scene')

  mse = np.mean((image - scene) ** 2)
  psnr = 100
  if(mse != 0):
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
  # print('cmp_psnr mse,psnr:', mse,  psnr)
  data['psnr'] = psnr 
  return data


def cmp_norm(params: Dict, **data: Dict) -> Dict:
  '''
  Calculates 'Pixels difference' between two GRAY images.
  This two images must have the same dimension.

  Parameters:
    - params:
    - data: 
      image: np.dtype; the first image
      scene: np.dtype; the second image
  Returns:
    - data:
      diff: float; Difference
  '''  

  image = data.get('image')
  scene = data.get('scene')
  norm = image/np.sqrt(np.sum(image**2))  
  norm1 = scene/np.sqrt(np.sum(scene**2))  
  diff =np.sum(norm*norm1)
  # print('cmp_norm diff:', diff)
  data['diff'] = diff 

  # https://stackoverflow.com/questions/11541154/checking-images-for-similarity-with-opencv
  # picture1 = np.random.rand(100,100)
  # picture2 = np.random.rand(100,100)
  # picture1_norm = picture1/np.sqrt(np.sum(picture1**2))
  # picture2_norm = picture2/np.sqrt(np.sum(picture2**2))
  # print(np.sum(picture1_norm*picture2_norm))
  return data


