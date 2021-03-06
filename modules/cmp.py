'''
Compare operations
'''
import cv2
import numpy as np
# from skimage.measure import structural_similarity as ssim

def cpm_mse(**kwargs):
  '''
  Calculates 'Mean Squared Error' between pixels of two images.
  The 'Mean Squared Error' between the two images is the
  sum of the squared difference between the two images.
  This two images must have the same dimension.

  Keyword arguments (key, default):
  - image: an original image;
  - image: an image to compare;

  Returns:
  - images;
  - mse: Mean Squared Errors.
  '''  

  err = np.sum((kwargs['image'].astype("float") - kwargs['image1'].astype("float")) ** 2)
  err /= float(kwargs['image'].shape[0] * kwargs['image'].shape[1])

  kwargs['mse'] = err

  return kwargs


def cmp_ssim(**kwargs):
  '''
  Calculates 'Structural Similarity Index' between pixels of two images.
  Uses to compare two windows instead an entire images.

  Keyword arguments (key, default):
  - image: an original image;
  - image: an image to compare;

  Returns:
  - images;
  - ssim: Structural Similarity Index.
  '''  

  # s = ssim(kwargs['image'], kwargs['image1'])
  # kwargs['ssim'] = None 

  return kwargs
