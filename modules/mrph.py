'''
Morphological operations.
It is a set of non-linear operations that process 
images based on shapes morphology of features in an image. 
It applies structuring element to an input image and generate an output image.
'''
import cv2

def erode(**kwargs):
  '''
  Erodes away the boundaries of the foreground object and removes small-scale details 
  from an image but simultaneously reduces the size of regions of interest.
  This operation is opposite to dilation

  Keyword arguments (key, default):
  - image: an image;
  - iter: number of iterations, 3;

  Returns:
  - image: result image;
  '''

  iterations = kwargs.get('iter', 3)

  erode = cv2.erode(kwargs['image'], None, iterations=iterations)
  kwargs['image'] = erode
  
  return kwargs


def dilate(**kwargs):
  '''
  Probings and expands the shapes contained in the input image. 
  This operation is opposite to erosion
  
  Keyword arguments (key, default):
  - image: an image;
  - iter: number of iterations, 3;

  Returns:
  - image: result image;
  '''

  iterations = kwargs.get('iter', 3)

  dilate = cv2.dilate(kwargs['image'], None, iterations=iterations)

  kwargs['image'] = dilate
  
  return kwargs


def mex(**kwargs):
  '''
  Performs one of following morphological operations:
  - opening: erosion followed by dilation;
  - closing: dilation followed by erosion;
  - gradient: the difference between dilation and erosion of an image.
  - top hat: the difference between input image and opening of the image.
  - black hat: the difference between the closing of the input image and input image.

  Keyword arguments (key, default):
  - image: an image;
  - shape: shape of structuring element, 0:
    - cv2.MORPH_RECT: 0;
    - cv2.MORPH_CROSS: 1;
    - cv2.MORPH_ELLIPSE: 2.
  - type: type of operations, 2:
    - cv2.MORPH_OPEN: 2;
    - cv2.MORPH_CLOSE: 3;
    - cv2.MORPH_GRADIENT: 4;
    - cv2.MORPH_TOPHAT: 5;
    - cv2.MORPH_BLACKHAT: 6; 
  - k: kernel size (3, 3), (5, 5), (7, 7), 3.

  Returns:
  - image: result image;
  '''
  
  shape = kwargs.get('shape',cv2.MORPH_RECT)
  type = kwargs.get('type', cv2.MORPH_OPEN)
  kernelSize = kwargs.get('k', 3)

  kernel = cv2.getStructuringElement(shape, (kernelSize, kernelSize))

  mrph = cv2.morphologyEx(kwargs['image'], type, kernel)

  kwargs['mrph'] = mrph 

  return kwargs



