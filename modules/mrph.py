'''
Morphological operations.
It is a set of non-linear operations that process 
images based on shapes morphology of features in an image. 
It applies structuring element to an input image and generate an output image.
  kernel: Creates a structured element (kernel)
  erode: Erodes away the boundaries of the foreground object and removes small-scale details 
    from an image but simultaneously reduces the size of regions of interest
  dilate: Probings and expands the shapes contained in the input image
  mex: operations:
    opening: erosion followed by dilation,
    closing: dilation followed by erosion
    gradient: the difference between dilation and erosion of an image
    top hat: the difference between input image and opening of the image
    black hat: the difference between the closing of the input image and input image
'''

from typing import Dict
import cv2


def kernel(params: Dict , **data: Dict) -> Dict:
  '''
  Creates a structured element (kernel)

    Parameters:
    - params:   
      shape: Dict[str,int](RECT:0,CROSS:1,ELLIPSE:2)=RECT; shape of structuring element cv2.MORPH_(...)
      kernel: Scale[int](3,13,1,1)=3; kernel size
    - data: 
  Returns:
    - data:
      kernel: ndarray; structured element (kernel)
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
      image: ndarray; the image
      kernel: ndarray; structured element (kernel)
  Returns:
    - data:
      erode: ndarray; the result image
  '''

  iterations = params.get('iter', 1)
  kernel = data.get('kernel')
  image = data.get('image')

  mrpherode = cv2.erode(image, kernel, iterations=iterations)
  data['erode'] = mrpherode
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
      image: ndarray; the image
      kernel: ndarray; structured element (kernel)
  Returns:
    - data:
      dilate: ndarray; the result image
  '''

  iterations = params.get('iter', 1)
  kernel = data.get('kernel')
  mrphdilate = cv2.dilate(data.get('image'), kernel, iterations=iterations)
  data['dilate'] = mrphdilate
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
      image: ndarray; the image
      kernel: ndarray; structured element (kernel)
  Returns:
    - data:
      mex: ndarray; the result image
  ''' 

  type = params.get('type', cv2.MORPH_OPEN)
  kernel = data.get('kernel')
  mrphex = cv2.morphologyEx(data['image'], type, kernel) 
  data['mex'] = mrphex
  return data



# # Get the circle region when given the center, you could try the following function:
# def circle_average(center, r = 4):
#     for i in range(center[0]-r, center[0]+r):
#         for j in range(center[1]-r, center[1] + r):
#             if (center[0] - i) ** 2 + (center[1] - j) ** 2 <= r**2:
#                # do your computation here.