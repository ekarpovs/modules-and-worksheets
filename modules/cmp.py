'''
Compare operations
'''
import cv2
import numpy as np
from skimage.measure import compare_ssim
# from skimage.measure import structural_similarity as ssim
from math import log10, sqrt

def cmp_mse(**kwargs):
  '''
  Calculates 'Mean Squared Error' between pixels of two images.
  The 'Mean Squared Error' between the two images is the
  sum of the squared difference between the two images.
  This two images must have the same dimension.

  Keyword arguments (key, default):
  - image: an original image;
  - image1: an image to compare;

  Returns:
  - images;
  - mse: Mean Squared Errors.
  '''  

  err = np.sum((kwargs['image'].astype("float") - kwargs['image1'].astype("float")) ** 2)
  err /= float(kwargs['image'].shape[0] * kwargs['image'].shape[1])

  kwargs['mse'] = err

  print("mse error", err)

  return kwargs


def cmp_ssim(**kwargs):
  '''
  Calculates 'Structural Similarity Index' between pixels of two images.
  Uses to compare two windows instead an entire images.
  This two images must have the same dimension.

  Keyword arguments (key, default):
  - image: an original image;
  - image1: an image to compare;

  Returns:
  - images;
  - ssim: Structural Similarity Index.
  '''  

  s, diff = compare_ssim(kwargs['image'], kwargs['image1'], full=True, multichannel=True)
  kwargs['ssim'] = s 

  print("ssim", s)

  return kwargs


def cmp_psnr(**kwargs):
  '''
  Calculates 'Peak Signal-to-Noise Ratio' between two images.
  This two images must have the same dimension.

  Keyword arguments (key, default):
  - image: an original image;
  - image1: an image to compare;

  Returns:
  - images;
  - psnr: Peak Signal-to-Noise Ratio.
  '''  

  mse = np.mean((kwargs['image'] - kwargs['image1']) ** 2)
  psnr = 100
  if(mse != 0):
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))

  kwargs['psnr'] = psnr 

  print("psnr", psnr)

  return kwargs


def cmp_norm(**kwargs):
  '''
  Calculates 'Pixels difference' between two GRAY images.
  This two images must have the same dimension.

  Keyword arguments (key, default):
  - image: an original image;
  - image1: an image to compare;

  Returns:
  - images;
  - psnr: Difference.
  '''  
  image = kwargs['image']
  image1 = kwargs['image1']

  norm = image/np.sqrt(np.sum(image**2))  
  norm1 = image1/np.sqrt(np.sum(image1**2))  
  diff =np.sum(norm*norm1)
  
  kwargs['diff'] = diff 

  print("diff", diff)

  # https://stackoverflow.com/questions/11541154/checking-images-for-similarity-with-opencv
  # picture1 = np.random.rand(100,100)
  # picture2 = np.random.rand(100,100)
  # picture1_norm = picture1/np.sqrt(np.sum(picture1**2))
  # picture2_norm = picture2/np.sqrt(np.sum(picture2**2))
  # print(np.sum(picture1_norm*picture2_norm))

  return kwargs


