'''
Morphological operations.
It is a set of non-linear operations that process 
images based on shapes morphology of features in an image. 
It applies structuring element to an input image and generate an output image.
'''
import cv2



def kernel(step, **kwargs):
  '''
  Create structured element (kernel)

  Keyword arguments:
  - image: an image;

  Step arguments (--Type:Domain:[Possible Values]:Default-- name: description):
  --n;d;[RECT:0,CROSS:1,ELLIPSE:2];RECT-- shape: shape of structuring element cv2.MORPH_(...)
  --n;l;[3,5,7,9];3-- k: kernel size

  Returns:
  - image: result image;
  - elem
  '''

  shape = step.get('shape',cv2.MORPH_RECT)
  kernelSize = step.get('k', 3)

  kernel = cv2.getStructuringElement(shape, ksize=(kernelSize, kernelSize))

  kwargs['kernel'] = kernel
  
  return kwargs


def erode(step, **kwargs):
  '''
  Erodes away the boundaries of the foreground object and removes small-scale details 
  from an image but simultaneously reduces the size of regions of interest.
  This operation is opposite to dilation

  Keyword arguments:
  - image: an image;
  - kernel: a kernel;

  Step arguments (--Type:Domain:[Possible Values]:Default-- name: description):
  --n;r;[1,15,1];1-- iter: number of iterations

  Returns:
  - image: result image;
  '''

  iterations = step.get('iter', 1)

  kernel = kwargs.get('kernel')
  mrpherode = cv2.erode(kwargs.get('image'), kernel, iterations=iterations)
  
  kwargs['image'] = mrpherode
  
  return kwargs



def dilate(step, **kwargs):
  '''
  Probings and expands the shapes contained in the input image. 
  This operation is opposite to erosion
  
  Keyword arguments:
  - image: an image;
  - kernel: a kernel;

  Step arguments (--Type:Domain:[Possible Values]:Default-- name: description):
  --n;r;[1,15,1];1-- iter: number of iterations

  Returns:
  - image: result image;
  '''

  iterations = step.get('iter', 1)

  kernel = kwargs.get('kernel')
  mrphdilate = cv2.dilate(kwargs.get('image'), kernel, iterations=iterations)

  kwargs['image'] = mrphdilate

  return kwargs



def mex(step, **kwargs):
  '''
  Performs one of following morphological operations:
  - opening: erosion followed by dilation;
  - closing: dilation followed by erosion;
  - gradient: the difference between dilation and erosion of an image.
  - top hat: the difference between input image and opening of the image.
  - black hat: the difference between the closing of the input image and input image.

  Keyword arguments:
  - image: an image;
  - kernel: a kernel;

  Step arguments (--Type:Domain:[Possible Values]:Default-- name: description):
  --n;d;[OPEN:2,CLOSE:3,GRADIENT:4,TOPHAT:5,BLACKHAT:6];OPEN-- type: type of operations cv2.MORPH_(...)

  Returns:
  - image: result image;
  '''
  
  type = step.get('type', cv2.MORPH_OPEN)

  kernel = kwargs.get('kernel')
  mrphex = cv2.morphologyEx(kwargs['image'], type, kernel)
  
  kwargs['image'] = mrphex

  return kwargs



