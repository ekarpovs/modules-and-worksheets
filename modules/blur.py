import cv2
# Bluring operation

def avg(input_, **kwargs):

  kernel = kwargs.get('k', 3)
  kX = kY = kernel 

  output_ = cv2.blur(input_, (kX, kY)) 

  return output_


def gaus(input_, **kwargs):

  kernel = kwargs.get('k', 3)
  kX = kY = kernel 

  output_ = cv2.GaussianBlur(input_, (kX, kY), 0)

  return output_


def median(input_, **kwargs):

  kernel = kwargs.get('k', 3)

  output_ = cv2.medianBlur(input_, kernel)

  return output_
