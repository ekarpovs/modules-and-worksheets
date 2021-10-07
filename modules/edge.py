'''
Gradient and edge dectection operations
Gradient magnitude and orientation.
'''
import cv2
import numpy as np

def sobel(params, **data):
  '''
  Computes gradients along the X or Y axis uses Sobel algorithm.

    parameters:
    - params: 
      --n;d;[horizontal:0,vertical:1];horizontal-- direction: direction (x, y));

    - data: 
        image - reference to the image
  returns:
    - data: 
        image - reference to the result image
  '''
  direction = params.get('direction', 0)
  dx = 1
  dy = 0
  if direction == 1:
    dx = 0
    dy = 1
  # compute gradients along the X or Y axis
  g = cv2.Sobel(data.get('image'), ddepth=cv2.CV_64F, dx=dx, dy=dy) 
  # images are now of the floating point data type,
  # so convert them back a to unsigned 8-bit integer representation
  data['image'] = cv2.convertScaleAbs(g)
  return data


def canny(params, **data):
  '''
  Computes a "wide", "mid-range", and "tight" threshold for the edges.

  parameters:
    - params: 
      --n;r;[10,150,1];50-- thrs1: threshold1;
      --n;r;[100,252,1];200-- thrs2: threshold2;
    - data: 
        image - reference to the image
  returns:
    - data: 
        image - reference to the result image
  '''
  threshold1 = params.get('thrs1', 10)
  threshold2 = params.get('thrs2', 200)
  data['image'] = cv2.Canny(data.get('image'), threshold1, threshold2)
  return data


def laplacian(params, **data):
  '''
  Computes the Laplacian of the image .

  parameters:
    - params: 
    - data: 
        image - reference to the image
  returns:
    - data: 
        image - reference to the result image
  '''
  lap = cv2.Laplacian(data.get('image'), cv2.CV_64F)
  data['image'] = np.uint8(np.absolute(lap)) 
  return data

#scharr
#norm_factor = 32
#gradx = cv2.Scharr(img, cv2.CV_32F, 1, 0, scale=1.0/norm_factor)
#grady = cv2.Scharr(img, cv2.CV_32F, 0, 1, scale=1.0/norm_factor)


#prewitt
#kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
#kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
#img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
#img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)