import cv2
# Bitwise operation

def and(**kwargs):
  kwargs['image'] = cv2.bitwise_and(kwargs['image'], kwargs['image1']) 

  return kwargs


def or(**kwargs):
  kwargs['image'] = cv2.bitwise_or(kwargs['image'], kwargs['image1']) 

  return kwargs


def xor(**kwargs):
  kwargs['image'] = cv2.bitwise_xor(kwargs['image'], kwargs['image1']) 

  return kwargs


def not(**kwargs):
  kwargs['image'] = cv2.bitwise_not(kwargs['image'], kwargs['image1']) 

  return kwargs