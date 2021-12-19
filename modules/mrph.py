'''
Morphological operations.
It is a set of non-linear operations that process 
images based on shapes morphology of features in an image. 
It applies structuring element to an input image and generate an output image.
'''

from typing import Dict
import cv2


def kernel(params: Dict , **data: Dict) -> Dict:
  '''
  Creates structured element (kernel)

    Parameters:
    - params:   
      shape: Dict[str,int](RECT:0,CROSS:1,ELLIPSE:2)=RECT; shape of structuring element cv2.MORPH_(...)
      kernel: Scale[int](3,13,1,1)=3; kernel size
    - data: 
      image: array[dtype[uint8]]; the image
  Returns:
    - data:
      kernel: List[bool]; structured element (kernel)
  '''

  shape = params.get('shape',cv2.MORPH_RECT)
  kernel_size = params.get('kernel', 3)
  kernel = cv2.getStructuringElement(shape, ksize=(kernel_size, kernel_size))
  data['kernel'] = kernel
  return data


def erode(params: Dict , **data: Dict) -> Dict:
  '''
  Erodes away the boundaries of the foreground object and removes small-scale details 
  from an image but simultaneously reduces the size of regions of interest.
  This operation is opposite to dilation

    Parameters:
    - params:   
      iter: Scale[int](1,15,1,0)=1; number of iterations
    - data: 
      image: array[dtype[uint8]]; the image
      kernel: List[bool]; structured element (kernel)
  Returns:
    - data:
      image: array[dtype[uint8]]; the result image
  '''

  iterations = params.get('iter', 1)
  kernel = data.get('kernel')
  mrpherode = cv2.erode(data.get('image'), kernel, iterations=iterations)
  data['image'] = mrpherode
  return data


def dilate(params: Dict , **data: Dict) -> Dict:
  '''
  Probings and expands the shapes contained in the input image. 
  This operation is opposite to erosion
  
  parameters:
    - params: 
    Parameters:
    - params:   
      iter: Scale[int](1,15,1,0)=1; number of iterations
    - data: 
      image: array[dtype[uint8]]; the image
      kernel: List[bool]; structured element (kernel)
  Returns:
    - data:
      image: array[dtype[uint8]]; the result image
  '''
  iterations = params.get('iter', 1)
  kernel = data.get('kernel')
  mrphdilate = cv2.dilate(data.get('image'), kernel, iterations=iterations)
  data['image'] = mrphdilate
  return data


def mex(params: Dict , **data: Dict) -> Dict:
  '''
  Morphological operations:
  - opening: erosion followed by dilation;
  - closing: dilation followed by erosion;
  - gradient: the difference between dilation and erosion of an image.
  - top hat: the difference between input image and opening of the image.
  - black hat: the difference between the closing of the input image and input image.

    Parameters:
    - params:   
      type: Dict[str,int](OPEN:2,CLOSE:3,GRADIENT:4,TOPHAT:5,BLACKHAT:6)=OPEN; type of operations cv2.MORPH_(...)
    - data: 
      image: array[dtype[uint8]]; the image
      kernel: List[bool]; structured element (kernel)
  Returns:
    - data:
      image: array[dtype[uint8]]; the result image
  ''' 

  type = params.get('type', cv2.MORPH_OPEN)
  kernel = data.get('kernel')
  mrphex = cv2.morphologyEx(data['image'], type, kernel) 
  data['image'] = mrphex
  return data



