import cv2

def bgrto(**kwargs):  
  """
  # Possible conversion types:
  # cv2.COLOR_BGR2GRAY 6
  # cv2.COLOR_BGR2HSV 40
  # cv2.COLOR_BGR2LAB 44
  # cv2.COLOR_BGR2BGRA 0
  # cv2.COLOR_BGR2RGB 4
  # cv2.COLOR_BGR2XYZ 32
  # cv2.COLOR_BGR2YCrCb 36
  # cv2.COLOR_BGR2Luv 50
  # cv2.COLOR_BGR2HLS 52
  # cv2.COLOR_BGR2YUV 82
  """

  type = kwargs.get('type', cv2.COLOR_BGR2GRAY)
  kwargs.pop('type', None)

  if len(kwargs['image'].shape) == 2:
  
    # input - gray
    return kwargs

  kwargs['image'] = cv2.cvtColor(kwargs['image'], type)

  return kwargs
