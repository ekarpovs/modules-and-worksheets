import cv2
# Smoothing operation

def bilateral(input_, **kwargs):
  """
  # diameter, sigmaColor, sigmaSpace
  (11, 21, 7)
  (11, 41, 21)
  (11, 61, 39)
  """
  diameter = kwargs.get('d', 11)
  sigmaColor = kwargs.get('c', 21)
  sigmaSpace = kwargs.get('s', 7)

  output_ = cv2.bilateralFilter(input_, diameter, sigmaColor, sigmaSpace)

  return output_
