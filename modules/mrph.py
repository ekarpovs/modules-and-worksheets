import cv2
# Morphological operation

def erode(**kwargs):
  """
  iterations > 0 
  """
  iterations = kwargs.get('iter', 3)

  kwargs['image'] = cv2.erode(kwargs['image'], None, iterations=iterations)

  return kwargs


def dilate(**kwargs):
  """
  iterations > 0 
  """
  iterations = kwargs.get('iter', 3)

  kwargs['image'] = cv2.dilate(kwargs['image'], None, iterations=iterations)

  return kwargs


def mex(**kwargs):
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
  kwargs.pop('shape', None)
  kwargs.pop('type', None)
  kwargs.pop('k', None)

  kernel = cv2.getStructuringElement(shape, (kernelSize, kernelSize))

  kwargs['image'] = cv2.morphologyEx(kwargs['image'], type, kernel) 

  return kwargs



