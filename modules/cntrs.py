'''
Contours oprations
'''
import cv2

def find(**kwargs):
  '''
  Finds contours of an image.
  Gets via kwargs (key, default value): 
    - image;
    - mth - approximation method, 2:
      cv2.CHAIN_APPROX_NONE - 1
      cv2.CHAIN_APPROX_SIMPLE - 2
      cv2.CHAIN_APPROX_TC89_L1 - 3
      cv2.CHAIN_APPROX_TC89_KCOS - 4
    - md - result mode, 0:
      cv2.RETR_EXTERNAL - 0
      cv2.RETR_LIST - 1
      cv2.RETR_CCOMP - 2
      cv2.RETR_TREE - 3
      cv2.RETR_FLOODFILL - 4
  Returns image and list of contours.
  '''  

  mode = kwargs.get('md', cv2.RETR_EXTERNAL)
  method = kwargs.get('mth', cv2.CHAIN_APPROX_SIMPLE)

  kwargs['cntrs'] = cv2.findContours(kwargs['image'], mode, method) 

  return kwargs