import cv2
import numpy as np
from skimage.measure import structural_similarity as ssim
# Compare operations

def mse(**kwargs):
  # the 'Mean Squared Error' between the two images is the
  # sum of the squared difference between the two images;
  # the two images must have the same dimension
  err = np.sum((kwargs['image'].astype("float") - kwargs['image1'].astype("float")) ** 2)
  err /= float(kwargs['image'].shape[0] * kwargs['image'].shape[1])

  kwargs['mse'] = err

  return kwargs


def ssim(**kwargs):
  # The 'Structural Similarity Index' used to compare two windows instead an entire image
  s = ssim(kwargs['image'], kwargs['image1'])
  kwargs['ssim'] = None 

  return kwargs
