import cv2

# Simple threshold operations

def simple(input_, **kwargs):
  """
  cv2.THRESH_BINARY 0
  THRESH_BINARY_INV 1
  """

  type = kwargs.get('type', cv2.THRESH_BINARY)
  threshold = kwargs.get('thrsh', 127)
  
  (T, output_) = cv2.threshold(input_, threshold, 255, type)

  return output_
