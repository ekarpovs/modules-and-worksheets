'''
Smoothing operation
'''
import cv2


def bilateral(step, **kwargs):
  '''
  Applies bilateral filtering to the input image

  Keyword arguments:
  - image: an image;

  Step arguments (--Type;Domain;[Possible Values];Default-- name: description):
  --n;s;[];11-- d: diameter of each pixel neighborhood that is used during filtering
  --n;l;[21,41,61];21--c: filter sigma in the color space
  --n;l;[7,21,39];21-- s: filter sigma in the coordinate space

  Returns:
  - image: result image;
  '''

  diameter = step.get('d', 11)
  sigmaColor = step.get('c', 21)
  sigmaSpace = step.get('s', 7)

  kwargs['image'] = cv2.bilateralFilter(kwargs['image'], diameter, sigmaColor, sigmaSpace)
   
  return kwargs
