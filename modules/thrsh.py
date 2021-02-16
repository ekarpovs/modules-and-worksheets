import cv2

# Simple threshold operations

def simple(**kwargs):
  """
  cv2.THRESH_BINARY 0
  THRESH_BINARY_INV 1
  """

  type = kwargs.get('type', cv2.THRESH_BINARY)
  threshold = kwargs.get('thrsh', 127)

  (T, kwargs['image']) = cv2.threshold(kwargs['image'], threshold, 255, type)

  return kwargs
