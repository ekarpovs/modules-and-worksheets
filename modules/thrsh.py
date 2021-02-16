import cv2

# Threshold operations

def simple(**kwargs):
  """
  cv2.THRESH_BINARY 0
  cv2.THRESH_BINARY_INV 1
  cv2.THRESH_TRUNC 2
  cv2.THRESH_TOZERO 3
  cv2.THRESH_TOZERO_INV 4
  """

  type = kwargs.get('type', cv2.THRESH_BINARY)
  threshold = kwargs.get('thrsh', 127)

  (T, kwargs['image']) = cv2.threshold(kwargs['image'], threshold, 255, type)

  return kwargs


def otsu(**kwargs):
  """
  cv2.THRESH_BINARY 0
  cv2.THRESH_BINARY_INV 1
  cv2.THRESH_TRUNC 2
  cv2.THRESH_TOZERO 3
  cv2.THRESH_TOZERO_INV 4
  cv2.THRESH_OTSU 8
  """

  type = kwargs.get('type', cv2.THRESH_BINARY) | cv2.THRESH_OTSU

  (T, kwargs['image']) = cv2.threshold(kwargs['image'], 0, 255, type)

  return kwargs


def adaptive(**kwargs):
  """
  cv2.THRESH_BINARY 0
  cv2.THRESH_BINARY_INV 1
  cv2.THRESH_TRUNC 2
  cv2.THRESH_TOZERO 3
  cv2.THRESH_TOZERO_INV 4
  cv2.ADAPTIVE_THRESH_MEAN_C 0
  cv2.ADAPTIVE_THRESH_GAUSSIAN_C 1 
  """

  type = kwargs.get('type', cv2.THRESH_BINARY) 
  method = kwargs.get('mth', cv2.ADAPTIVE_THRESH_MEAN_C) 
  na = kwargs.get('na',15) # neighborhood area
  c = kwargs.get('c', 5) #  It is just a constant which is subtracted from the mean or weighted mean calculated.

  kwargs['image'] = cv2.adaptiveThreshold(kwargs['image'], 255, method, type, na, c)

  return kwargs
