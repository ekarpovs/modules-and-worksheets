import cv2
# Smoothing operation

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
  kwargs.pop('d', None)
  kwargs.pop('c', None)
  kwargs.pop('s', None)

  kwargs['image'] = cv2.bilateralFilter(kwargs['image'], diameter, sigmaColor, sigmaSpace)

  return kwargs
