import cv2
# Gradient and edge dectection operation
# gradient magnitude and orientation

def sobel(input_, **kwargs):
  """
  direction 
  x 0
  y 1 
  """

  direction = kwargs.get('d', 0)
  dx = 1
  dy = 0
  if direction == 1:
    dx = 0
    dy = 1

  # compute gradients along the X or Y axis
  g = cv2.Sobel(input_, ddepth=cv2.CV_64F, dx=dx, dy=dy) 
  # images are now of the floating point data type,
  # so convert them back a to unsigned 8-bit integer representation
  output_ = cv2.convertScaleAbs(g)

  return output_


# compute a "wide", "mid-range", and "tight" threshold for the edges
def canny(input_, **kwargs):
  """
  wide, mid, tight
  threshold1 10, 30, 240
  threshold2 200, 150, 250
  """

  threshold1 = kwargs.get('thrs1', 10)
  threshold2 = kwargs.get('thrs2', 200)

  output_ = cv2.Canny(input_, threshold1, threshold2)
  
  return output_