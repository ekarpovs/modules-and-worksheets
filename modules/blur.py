'''
Bluring operation
'''
import cv2


def avg(params, **data):
  '''
  Average bluring.

  parameters:
    - params:
      --n;l;[3,5,7,9];3-- k: kernel size   
    - data: 
      image - reference to an image that will be blured
  returns:
    - data:
      image - reference to the blured image
  '''
  kernel = params.get('k', 3)
  kX = kY = kernel 
  data['image'] = cv2.blur(data.get('image'), (kX, kY)) 
  return data


def gaus(params, **data):
  '''
  Gausian bluring.

  parameters:
    - params:
      --n;l;[3,5,7,9];3-- k: kernel size   
    - data: 
      image - reference to an image that will be blured
  returns:
    - data:
      image - reference to the blured image
  '''
  kernel = params.get('k', 3)
  kX = kY = kernel 
  data['image'] = cv2.GaussianBlur(data.get('image'), (kX, kY), 0)
  return data



def median(params,**data):
  '''
  Median bluring.

    parameters:
    - params:
      --n;l;[3,5,7,9];3-- k: kernel size   
    - data: 
      image - reference to an image that will be blured
  returns:
    - data:
      image - reference to the blured image
'''
  kernel = params.get('k', 3)
  data['image'] = cv2.medianBlur(data.get('image'), kernel)
  return data
