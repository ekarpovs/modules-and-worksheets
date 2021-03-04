'''
Smoothing operation
'''
import cv2

def bilateral(**kwargs):
  """
  # diameter, sigmaColor, sigmaSpace
  (11, 21, 7)
  (11, 41, 21)
  (11, 61, 39)
  """
  diameter = kwargs.get('d', 11)
  sigmaColor = kwargs.get('c', 21)
  sigmaSpace = kwargs.get('s', 7)

  kwargs['image'] = cv2.bilateralFilter(kwargs['image'], diameter, sigmaColor, sigmaSpace)

  return kwargs
