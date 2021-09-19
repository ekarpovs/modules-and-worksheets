'''
Basic operations
'''
import cv2
import numpy as np


def crop(params, **data):
  '''
  Crops an image.

  parameters:
    - params:
      --n;s;[];0-- y0: left top coordinate
      --n;s;[];h-- y1: left bottom coordinate
      --n;s;[];0-- x0: left top coordinate
      --n;s;[];w-- x1: Right top coordinate
    
    - data:
      image - reference to an image that will be cropped

  returns:
    - data:
      image - reference to the cropped image
  '''  
  image = data.get('image')
  (h, w) = image.shape[:2]

  y0 = params.get('y0', 0)
  y1 = params.get('y1', h)
  x0 = params.get('x0', 0)
  x1 = params.get('x1', w)

  data['image'] = image[y0:y1, x0:x1]
  return data

def flip(params, **data):
  '''
  Flips an image.

  parameters:
    - params:
      --n;d;[both:0,vertical:1,horizontal:2];vertical-- direct: direction
    
    - data: 
      image - reference to an image that will be flipped

  returns:
    - data:
      image - reference to the flipped image
  '''  
  direction = params.get('direct', 1)

  data['image'] = cv2.flip(data.get('image'), direction) 
  return data


def resize(params, **data):
  '''
  Resizes an image.

  parameters:
    - params:
      --n;d;[NEAREST:0,LINEAR:1,AREA:2,CUBIC:3,LANCZOS:4];AREA-- meth: interpolation method cv2.INTER_(...)
      --n;d;[pixel:0,percent:1];pixel-- unit: measurements unit
      --n;d;[height:0,width:1];height-- side: rectangle side
      --n;s;[];h/w-- size: new zise
    
    - data: 
      image - reference to an image that will be resized

  returns:
    - data:
      image - reference to the resized image
  '''
  method = params.get('meth', cv2.INTER_AREA)
  unit = params.get('unit', 0)
  side = params.get('side', 0)

  image = data.get('image')
  (h, w) = image.shape[:2]
  #  default value regarding to the side of a rectangle
  def_size = w
  if side == 0:
    def_size = h
  size = int(params.get('size', def_size))
  if unit == 1:
    # size defined in percents - calculate in pixels
    orig_pixels = w
    if side == 1:
      orig_pixels = h

    size = int((orig_pixels / 100) * size)
  
  #  the ratio of the new image to the old image, regarding to the side of a rectangle
  ratio = size / w
  dim = (size, int(h * ratio))
  if side == 0:
    ratio = size / h
    dim = (int(w * ratio), size)

  data['image'] = cv2.resize(image, dim, interpolation=method) 
  return data


def resize1(params, **data):
  '''
  Resizes an image without aspect ratio (absolute resizing).

  parameters:
    - params:
      --n;d;[NEAREST:0,LINEAR:1,AREA:2,CUBIC:3,LANCZOS:4];AREA-- meth: interpolation method cv2.INTER_(...)
      --n;d;[pixel:0,percent:1];pixel-- unit: measurements unit
      --n;d;[height:0,width:1];height-- side: rectangle side
      --n;s;[];h/w-- size: new zise
    
    - data: 
      image - reference to an image that will be resized

  returns:
    - data:
      image - reference to the resized image

  '''  
  method = params.get('meth', cv2.INTER_AREA)
  unit = params.get('unit', 0)
  w_new = params.get('w', 9)
  h_new = params.get('h', 8)
  dim = (w_new, h_new)

  image = data.get('image')

  if unit == 1: # percent
    (h, w) = image.shape[:2]
    dim = (int(w*w_new/100), int(h*h_new/100))
    
  data['image'] = cv2.resize(image, dim, interpolation=method) 
  return data


def rotate(params, **data):  
  '''
  Rotates an image without cropping.
  
  parameters:
    - params:
      --n;r;[0,180,1];0-- angle: rotation angle
      --b;f;[False,True];True-- neg: negative direction 
    
    - data: 
      image - reference to an image that will be rotated

  returns:
    - data:
      image - reference to the rotaited image
  '''  
  # grab the dimensions of the image and calculate the center of the image
  image = data.get('image')
  (h, w) = image.shape[:2]
  (cx, cy) = (w / 2, h / 2)

  # calculate rotation matrix
  angle = params.get('angle', 0)
  negative = params.get('neg', False)
  if negative:
    angle *= -1 

  M = cv2.getRotationMatrix2D((cx, cy), angle, 1.0)
  # rotation calculates the cos and sin, taking absolutes of those.
  abs_cos = abs(M[0,0]) 
  abs_sin = abs(M[0,1])
  # find the new width and height bounds
  bound_w = int(h * abs_sin + w * abs_cos)
  bound_h = int(h * abs_cos + w * abs_sin)
  # subtract old image center (bringing image back to original relative position) and adding the new image center coordinates
  M[0, 2] += bound_w/2 - cx
  M[1, 2] += bound_h/2 - cy
  # rotate without a cropping
  data['image'] = cv2.warpAffine(image, M, (bound_w, bound_h))
  return data


def translate(params, **data):
  '''
  Translates (Shifts) an image by a NumPy matrix in the form:
    [[1, 0, shiftX], [0, 1, shiftY]] .

  parameters:
    - params:
      --n;s;[];0-- y: number of pixels to shift
      --n;s;[];0-- x: number of pixels to shift
    
    - data: 
      image - reference to an image that will be translated

  returns:
    - data:
      image - reference to the translated image
  '''  
  shiftX = params.get('x', 0)
  shiftY = params.get('y', 0)

  if shiftX == 0 and shiftY == 0:
    return data

  image = data.get('image')
  M = np.float32([[1, 0, shiftX], [0, 1, shiftY]])
  data['image'] = cv2.warpAffine(image, M, (image.shape[1], image.shape[0])) 
  return data


def fit(params, **data):
  '''
  Resizes image1 regarding image

  parameters:
    - params:
      --n;d;[NEAREST:0,LINEAR:1,AREA:2,CUBIC:3,LANCZOS:4];AREA-- meth: interpolation method cv2.INTER_(...)   
    - data: 
      image - reference to an image
      image1 - reference to an image that will be resized
  returns:
    - data:
      image - reference to the resized image
  '''  
  method = params.get('meth', cv2.INTER_AREA)
  image = data.get('image')
  (h, w) = image.shape[:2]
  image1 = data.get('image1')
  (h1, w1) = image1.shape[:2]
  if (h == h1 and w == w1):
    return data
  dim = (w, h)
  data['image'] = cv2.resize(image1, dim, interpolation=method) 
  return data


def transform(params, **data):
  '''
  Transforms a skewed image to obtain a top-down view of the original image

  parameters:
    - params:   
    - data: 
      image - reference to an image that will be transformed
  returns:
    - data:
      image - reference to the transformed image
  '''  
  rect_cnt = data['rect']
  data['image'] = _four_point_transform(data.get('image'), rect_cnt.reshape(4, 2)) 
  return data


############## Utils ###############################
# TODO: move to separate lib module 

def _order_points(pts):
  # initialzie a list of coordinates that will be ordered
  # such that the first entry in the list is the top-left,
  # the second entry is the top-right, the third is the
  # bottom-right, and the fourth is the bottom-left
  rect = np.zeros((4, 2), dtype = "float32")

  # the top-left point will have the smallest sum, whereas
  # the bottom-right point will have the largest sum
  s = pts.sum(axis = 1)
  rect[0] = pts[np.argmin(s)]
  rect[2] = pts[np.argmax(s)]

  # now, compute the difference between the points, the
  # top-right point will have the smallest difference,
  # whereas the bottom-left will have the largest difference
  diff = np.diff(pts, axis = 1)
  rect[1] = pts[np.argmin(diff)]
  rect[3] = pts[np.argmax(diff)]

  # return the ordered coordinates
  return rect

def _four_point_transform(image, pts):
  # obtain a consistent order of the points and unpack them
  # individually
  rect = _order_points(pts)

  (tl, tr, br, bl) = rect

  # compute the width of the new image, which will be the
  # maximum distance between bottom-right and bottom-left
  # x-coordiates or the top-right and top-left x-coordinates
  widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
  widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
  maxWidth = max(int(widthA), int(widthB))

  # compute the height of the new image, which will be the
  # maximum distance between the top-right and bottom-right
  # y-coordinates or the top-left and bottom-left y-coordinates
  heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
  heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
  maxHeight = max(int(heightA), int(heightB))

  # now that we have the dimensions of the new image, construct
  # the set of destination points to obtain a "birds eye view",
  # (i.e. top-down view) of the image, again specifying points
  # in the top-left, top-right, bottom-right, and bottom-left
  # order
  dst = np.array([
    [0, 0],
    [maxWidth - 1, 0],
    [maxWidth - 1, maxHeight - 1],
    [0, maxHeight - 1]], dtype = "float32")

  # compute the perspective transform matrix and then apply it
  M = cv2.getPerspectiveTransform(rect, dst)
  warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

  # return the warped image
  return warped