'''
Arithmetic operations
'''
import cv2
import numpy as np 


def arth_add(params, **data):
  '''
  Add operation with the input image and a mask

  parameters:
    - params:   
    - data: 
      image - reference to an source image
      mask - the second image
  returns:
    - data:
      image - reference to the result image
  '''
  mask = data.get('mask')
  data['image'] = cv2.add(data.get('image'), mask) 
  return data


def arth_sub(params, **data):
  '''
  Substraction operation with the input image and a mask

  parameters:
    - params:
      --n;s;[];1-- dfact: decrease factor   
    - data: 
      image - reference to an source image
      mask - the second image
  returns:
    - data:
      image - reference to the result image
  '''
  mask = data.get('mask')
  data['image'] = cv2.subtract(data.get('image'), mask) 
  return data
