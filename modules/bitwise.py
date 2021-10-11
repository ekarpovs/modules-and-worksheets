'''
Bitwise operations
'''
import cv2


def btw_and(params, **data):
  '''
  AND operation with an image and a mask.

  parameters:
    - params:  
    - data: 
      image - reference to an source image
      mask - the second image
  returns:
    - data:
      image - reference to the result image
  '''
  data['image'] = cv2.bitwise_and(data.get('image'), data.get('mask')) 
  return data



def btw_or(params, **data):
  '''
  OR operation with an image and a mask.

  parameters:
    - params:
    - data: 
      image - reference to an source image
      mask - the second image
  returns:
    - data:
      image - reference to the result image
  '''
  data['image'] = cv2.bitwise_or(data.get('image'), data.get('mask')) 
  return data



def btw_xor(params, **data):
  '''
  XOR operation with an image and a mask.

  parameters:
    - params:   
    - data: 
      image - reference to an source image
      mask - the second image
  returns:
    - data:
      image - reference to the result image
  '''
  data['image'] = cv2.bitwise_xor(data.get('image'), data.get('mask')) 
  return data



def btw_not(params, **data):
  '''
  NOT operation with an image and a mask.

  parameters:
    - params:   
    - data: 
      image - reference to an source image
      mask - the second image
  returns:
    - data:
      image - reference to the result image
  '''
  data['image'] = cv2.bitwise_not(data.get('image'), data.get('mask'))   
  return data