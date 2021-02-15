# Contours oprations
import cv2

def find(**kwargs):
  """
  cv2.RETR_EXTERNAL 0`
  cv2.RETR_LIST 1
  cv2.RETR_CCOMP 2
  cv2.RETR_TREE 3
  cv2.RETR_FLOODFILL 4
  "--------------")
  cv2.CHAIN_APPROX_NONE 1
  cv2.CHAIN_APPROX_SIMPLE 2
  cv2.CHAIN_APPROX_TC89_L1 3
  cv2.CHAIN_APPROX_TC89_KCOS 4
  """

  mode = kwargs.get('md', cv2.RETR_EXTERNAL)
  method = kwargs.get('mth', cv2.CHAIN_APPROX_SIMPLE)
  kwargs.pop('md', None)
  kwargs.pop('mth', None)

  kwargs['cntrs'] = cv2.findContours(kwargs['image'], mode, method) 

  return kwargs