import cv2
# Morphological operation

def erode(input_, **kwargs):
  """
  iterations > 0 
  """
  iterations = kwargs.get('iter', 3)

  for i in range(0, iterations):
    output_ = cv2.erode(input_, None, iterations=i + 1)

  return output_


def dilate(input_, **kwargs):
  """
  iterations > 0 
  """
  iterations = kwargs.get('iter', 3)

  for i in range(0, iterations):
    output_ = cv2.dilate(input_, None, iterations=i + 1)

  return output_


def mex(input_, **kwargs):
  """
  shape
  cv2.MORPH_RECT 0
  cv2.MORPH_CROSS 1
  cv2.MORPH_ELLIPSE 2
  type
  cv2.MORPH_OPEN 2
  cv2.MORPH_CLOSE 3
  cv2.MORPH_GRADIENT 4
  cv2
  kernelSizes (3, 3), (5, 5), (7, 7) 
  """

  shape = kwargs.get('shape',cv2.MORPH_RECT)
  type = kwargs.get('type', cv2.MORPH_OPEN)
  kernelSize = kwargs.get('k', 3)

  kernel = cv2.getStructuringElement(shape, (kernelSize, kernelSize))

  output_ = cv2.morphologyEx(input_, type, kernel) 

  return output_



