'''
Morphological operations.
It is a set of non-linear operations that process 
images based on shapes morphology of features in an image. 
It applies structuring element to an input image and generate an output image.
'''
import cv2



def kernel(params, **data):
  '''
  Creates structured element (kernel)

  parameters:
    - params: 
      --n;d;[RECT:0,CROSS:1,ELLIPSE:2];RECT-- shape: shape of structuring element cv2.MORPH_(...)
      --n;l;[3,5,7,9];3-- k: kernel size
    - data: 
        image - reference to the image
  returns:
    - data: 
        kernel - structured element (kernel)
  '''
  shape = params.get('shape',cv2.MORPH_RECT)
  kernelSize = params.get('k', 3)
  kernel = cv2.getStructuringElement(shape, ksize=(kernelSize, kernelSize))
  data['kernel'] = kernel
  return data


def erode(params, **data):
  '''
  Erodes away the boundaries of the foreground object and removes small-scale details 
  from an image but simultaneously reduces the size of regions of interest.
  This operation is opposite to dilation

  parameters:
    - params: 
      --n;r;[1,15,1];1-- iter: number of iterations
    - data: 
        image - reference to the image
        kernel - structured element (kernel)
  returns:
    - data: 
        image - result image;
  '''
  iterations = params.get('iter', 1)
  kernel = data.get('kernel')
  mrpherode = cv2.erode(data.get('image'), kernel, iterations=iterations)
  data['image'] = mrpherode
  return data


def dilate(params, **data):
  '''
  Probings and expands the shapes contained in the input image. 
  This operation is opposite to erosion
  
  parameters:
    - params: 
      --n;r;[1,15,1];1-- iter: number of iterations
    - data: 
        image - reference to the image
        kernel - structured element (kernel)
  returns:
    - data: 
        image - result image;
  '''
  iterations = params.get('iter', 1)
  kernel = data.get('kernel')
  mrphdilate = cv2.dilate(data.get('image'), kernel, iterations=iterations)
  data['image'] = mrphdilate
  return data


def mex(params, **data):
  '''
  Morphological operations:
  - opening: erosion followed by dilation;
  - closing: dilation followed by erosion;
  - gradient: the difference between dilation and erosion of an image.
  - top hat: the difference between input image and opening of the image.
  - black hat: the difference between the closing of the input image and input image.

  parameters:
    - params: 
      --n;d;[OPEN:2,CLOSE:3,GRADIENT:4,TOPHAT:5,BLACKHAT:6];OPEN-- type: type of operations cv2.MORPH_(...)
    - data: 
        image - reference to the image
        kernel - structured element (kernel)
  returns:
    - data: 
        image - result image;
  ''' 
  type = params.get('type', cv2.MORPH_OPEN)
  kernel = data.get('kernel')
  mrphex = cv2.morphologyEx(data['image'], type, kernel) 
  data['image'] = mrphex
  return data



