'''
Smoothing operation
'''
import cv2
from modules import flowoperation

@flowoperation
def bilateral(step, **kwargs):
  '''
  Applies bilateral filtering to the input image

  Keyword arguments (key, default):
  - image: an image;
  - d: diameter of each pixel neighborhood that is used during filtering, 11;
  - c: filter sigma in the color space, 21;
  - s: filter sigma in the coordinate space, 7.

  Values (d, c, s):
  - (11, 21, 7)
  - (11, 41, 21)
  - (11, 61, 39)

  Returns:
  - smshbil: result image;
  '''

  diameter = step.get('d', 11)
  sigmaColor = step.get('c', 21)
  sigmaSpace = step.get('s', 7)

  kwargs['image'] = cv2.bilateralFilter(kwargs['image'], diameter, sigmaColor, sigmaSpace)
   
  return kwargs
