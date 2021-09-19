'''
Compare operations
'''
import cv2
import numpy as np
from skimage.measure import compare_ssim
# from skimage.measure import structural_similarity as ssim
from math import log10, sqrt


def cmp_mse(params, **data):
  '''
  Calculates 'Mean Squared Error' between pixels of two images.
  The 'Mean Squared Error' between the two images is the
  sum of the squared difference between the two images.
  This two images must have the same dimension.

  parameters:
    - params:
      --str;s;[];image1--  key: name of a reference to the second image   
    - data: 
      image - reference to the first image
      key - reference to the second image
  returns:
    - data:
      mse - Mean Squared Errors.
  '''  
  key = params.get('key', 'image1')
  minuend = data.get('image')
  subtrahend = data.get(key)
  err = np.sum((minuend.astype("float") - subtrahend.astype("float")) ** 2)
  err /= float(minuend.shape[0] * minuend.shape[1])
  data['mse'] = err
  return data


def cmp_ssim(params, **data):
  '''
  Calculates 'Structural Similarity Index' between pixels of two images.
  Uses to compare two windows instead an entire images.
  This two images must have the same dimension.

  parameters:
    - params:
      --str;s;[];image1--  key: name of a reference to the second image
    - data: 
        image - reference to the first image
        key - reference to the second image
  returns:  
    - data: 
      ssim - Structural Similarity Index.
  '''  
  key = params.get('key', 'image1')
  image = data.get('image')
  image1 = data.get(key)
  s, diff = compare_ssim(image, image1, full=True, multichannel=True)
  data['ssim'] = s 
  return data


def cmp_psnr(params, **data):
  '''
  Calculates 'Peak Signal-to-Noise Ratio' between two images.
  This two images must have the same dimension.

  parameters:
    - params:
      --str;s;[];image1--  key: name of a reference to the second image
    - data: 
        image - reference to the first image
        key - reference to the second image
  returns:  
    - data: 
        psnr - Peak Signal-to-Noise Ratio.
  '''  
  key = params.get('key', 'image1')
  minuend = data.get('image')
  subtrahend = data.get(key)
  mse = np.mean((minuend - subtrahend) ** 2)
  psnr = 100
  if(mse != 0):
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
  data['psnr'] = psnr 
  return data


def cmp_norm(params, **data):
  '''
  Calculates 'Pixels difference' between two GRAY images.
  This two images must have the same dimension.

  parameters:
    - params:
      --str;s;[];image1--  key: name of a reference to the second image
    - data: 
        image - reference to the first image
        key - reference to the second image
  returns:  
    - data: 
        diff - Difference..
  '''  
  key = params.get('key', 'image1')
  image = data.get('image')
  image1 = data.get(key)
  norm = image/np.sqrt(np.sum(image**2))  
  norm1 = image1/np.sqrt(np.sum(image1**2))  
  diff =np.sum(norm*norm1)
  data['diff'] = diff 

  # https://stackoverflow.com/questions/11541154/checking-images-for-similarity-with-opencv
  # picture1 = np.random.rand(100,100)
  # picture2 = np.random.rand(100,100)
  # picture1_norm = picture1/np.sqrt(np.sum(picture1**2))
  # picture2_norm = picture2/np.sqrt(np.sum(picture2**2))
  # print(np.sum(picture1_norm*picture2_norm))
  return data


