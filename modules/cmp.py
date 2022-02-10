'''
Comparition operations
'''

from typing import Dict
import cv2
import numpy as np
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
      image: ndarray; the first image
      scene: ndarray; the second image
  Returns:
    - data:
      mse: float; Mean Squared Errors
  '''  

  image = data.get('image')
  scene = data.get('scene')
   
  # err = np.sum((image.astype("float") - scene.astype("float")) ** 2)
  # err /= float(image.shape[0] * image.shape[1])

  # err = np.square(np.subtract(image.astype("float"),scene.astype("float"))).mean()
  err = np.square(np.subtract(image, scene)).mean()

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
#       image: ndarray; the first image
#       scene: ndarray; the second image
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
      image: ndarray; the first image
      scene: ndarray; the second image
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
      image: ndarray; the first image
      scene: ndarray; the second image
  Returns:
    - data:
      diff: float; Difference
  '''  

  image = data.get('image')
  scene = data.get('scene')
  norm = image/np.sqrt(np.sum(image**2))  
  norm1 = scene/np.sqrt(np.sum(scene**2))  
  diff =np.sum(norm*norm1)
  data['diff'] = diff 

  # https://stackoverflow.com/questions/11541154/checking-images-for-similarity-with-opencv
  # picture1 = np.random.rand(100,100)
  # picture2 = np.random.rand(100,100)
  # picture1_norm = picture1/np.sqrt(np.sum(picture1**2))
  # picture2_norm = picture2/np.sqrt(np.sum(picture2**2))
  # print(np.sum(picture1_norm*picture2_norm))
  return data


def join(params: Dict, **data: Dict) -> Dict:
  '''
  Joins compare results

  Parameters:
    - params:
    - data: 
      mse: string; mse
      psnr: string; psnr
      diff: string; diff
  Returns:
    - data:
      cmp: Dict[str,str]; dictioanary of cmp results
  '''

  mse = data.get('mse','')
  psnr = data.get('psnr','')
  diff = data.get('diff','')
  cmp = {'mse': mse, 'psnr': psnr, 'diff': diff}
  data['cmp'] = cmp
  return data

def roi(params: Dict, **data: Dict) -> Dict:
  '''
  Gets ROI from an image.

  Parameters:
    - params:
      x0: int=0; top left corner of the ROI
      y0: int=0; top left corner of the ROI
      width: Scale[int](0,500,1,0)=1; width of the ROI
      wweight: Scale[int](0,10,1,0)=1; weight of width scale unit  
      height: Scale[int](0,700,1,0)=1; height of the ROI
      hweight: Scale[int](0,14,1,0)=1; weight of height scale unit  
    - data: 
      image: ndarray; the image
  Returns:
    - data:
      roi: ndarray; the roi
      roidef: Dict[str, str]; the roi defenition
  '''  

  x0 = params.get('x0', 0)
  y0 = params.get('y0', 0)
  width = params.get('width', 1)
  wweight = params.get('wweight', 1)
  height = params.get('height', 1)
  hweight = params.get('hweight', 1)

  image = data.get('image')
  (imh, imw) = image.shape[:2]

  # roi=cv2.selectROI(image)

  if width > 0 and height > 0:
    x1 = x0 + width*wweight
    y1 = y0 + height*hweight
    roi = image.copy()[y0:y1, x0:x1]   
  else:
    roi = image.copy()
  
  (h, w) = roi.shape[:2]
  data['roi'] = roi
  data['roidef'] = {'roidef': {
      'imwidth': imw,
      'imheight': imh,
      'x0': x0,
      'y0': y0,
      'width': width,
      'wweight': wweight,
      'height': height,
      'hweight': hweight
    }}

  return data


