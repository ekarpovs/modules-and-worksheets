'''
Basic operations
'''
import cv2
import numpy as np
from modules import flowoperation

@flowoperation
def crop(step, **kwargs):
  '''
  Crops an image.

  Keyword arguments (key, default):
  - image: an image;
  - y0 - left top coordinate, 0;
  - y1 - left right coordinate, h;
  - x0 - left top coordinate, 0;
  - x1 - left right coordinate, w.
  
  Returns:
  - bsccrop: result image;
  '''  

  (h, w) = kwargs['image'].shape[:2]

  y0 = step.get('y0', 0)
  y1 = step.get('y1', h)
  x0 = step.get('x0', 0)
  x1 = step.get('x1', w)

  kwargs['image'] = kwargs['image'][y0:y1, x0:x1]

  return kwargs


@flowoperation
def flip(step, **kwargs):
  '''
  Flipss an image.

  Keyword arguments (key, default):
  - image: an image;
  - drct: direction, 1.
 
  Returns:
  - bscflip: result image;
  - the kwargs as is.
  '''  
  direction = step.get('drct', 1)

  kwargs['image'] = cv2.flip(kwargs['image'], direction) 

  return kwargs


@flowoperation
def mask(step, **kwargs):
  '''
  Applys a mask to an image.

  Keyword arguments (key, default):
  - image: an image;
  - type - the mask shape (rectangle 0, circle 1) , 1;

    for rectangle:
    - y0 - left top coordinate, 0;
    - y1 - left right coordinate, h;
    - x0 - left top coordinate, 0;
    - x1 - left right coordinate, w.

    for circle:
    - cx - Center coordinate, w/2;
    - cy - Center coordinate, h/2;
    - rad - the mask radius,min(h / 2, w /2).
 
  Returns:
  - bscmask: result image;
  '''  
  (h, w) = kwargs['image'].shape[:2]

  type = step.get('type', 0)
  y0 = step.get('y0', 0)
  y1 = step.get('y1', h)
  x0 = step.get('x0', 0)
  x1 = step.get('x1', w)
  cx = step.get('cx', w / 2)
  cy = step.get('cy', h / 2)
  rad = step.get('rad', min(h / 2, w /2))
  
  # Masking allows us to focus only on parts of an image that interest us.
  # A mask is the same size as our image, but has only two pixel values,
  # 0 and 255. Pixels with a value of 0 are ignored in the orignal image,
  # and mask pixels with a value of 255 are allowed to be kept.
  mask = np.zeros(kwargs['image'].shape[:2], dtype="uint8")

  if type == 0:
    # Construct a rectangular mask
    cv2.rectangle(mask, (x0, y0), (x1, y1), 255, -1)
  else:
    # Make a circular mask
    cv2.circle(mask, (cx, cy), rad, 255, -1)

  # Apply out mask
  kwargs['image'] = cv2.bitwise_and(kwargs['image'], kwargs['image'], mask=mask)   

  return kwargs



@flowoperation
def resize(step, **kwargs):
  '''
  Resizes an image.

  Keyword arguments (key, default):
  - image: an image;
  
  - meth - interpolation method, 2:
    - cv2.INTER_NEAREST - 0;
    - cv2.INTER_LINEAR - 1;
    - cv2.INTER_AREA - 2;
    - cv2.INTER_CUBIC - 3;
    - cv2.INTER_LANCZOS4 - 4;
  - unit - measurements unit, 0:
    - pixel - 0;
    - percent - 1;
  - side - rectangle side, 0:
    - height 0
    - width 1
 
  Returns:
  - bscrsz: result image;
  '''

  (h, w) = kwargs['image'].shape[:2]

  method = step.get('meth', cv2.INTER_AREA)
  unit = step.get('unit', 0)
  side = step.get('side', 0)

  #  default value regarding to the side of a rectangle
  def_size = w
  if side == 0:
    def_size = h
  size = step.get('size', def_size)
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

  kwargs['image'] = cv2.resize(kwargs['image'], dim, interpolation=method) 

  return kwargs


@flowoperation
def resize1(step, **kwargs):
  '''
  Resizes an image without aspect ratio (absolute resizing).

  Keyword arguments (key, default):
  - image: an image;
  
  - meth - interpolation method, 2:
    - cv2.INTER_NEAREST - 0;
    - cv2.INTER_LINEAR - 1;
    - cv2.INTER_AREA - 2;
    - cv2.INTER_CUBIC - 3;
    - cv2.INTER_LANCZOS4 - 4;
  - unit - measurements unit, 0:
    - pixel - 0;
    - percent - 1;
  - side - rectangle side, 0:
    - height 0
    - width 1
 
  Returns:
  - bscrsz: result image;
  '''  

  method = step.get('meth', cv2.INTER_AREA)
  unit = step.get('unit', 0)
  w_new = step.get('w', 9)
  h_new = step.get('h', 8)

  dim = (w_new, h_new)
  if unit == 1: # percent
    (h, w) = kwargs['image'].shape[:2]
    dim = (int(w*w_new/100), int(h*h_new/100))
    
  kwargs['image'] = cv2.resize(kwargs['image'], dim, interpolation=method) 

  return kwargs


@flowoperation
def rotate(step, **kwargs):  
  '''
  Rotates an image without cropping.
  
  Keyword arguments (key, default):
  - image: an image;
  - angle: rotation angle, 0.

  Returns:
  - bscrot: result image;
  '''  

  # grab the dimensions of the image and calculate the center of the image
  (h, w, n) = kwargs['image'].shape
  (cx, cy) = (w / 2, h / 2)

  # calculate rotation matrix
  angle = step.get('angle', 0)
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
  kwargs['image'] = cv2.warpAffine(kwargs['image'], M, (bound_w, bound_h))

  return kwargs

@flowoperation
def translate(step, **kwargs):
  '''
  Translates (Shifts) an image by a NumPy matrix in the form:
    [[1, 0, shiftX], [0, 1, shiftY]] .

  Keyword arguments (key, default):
  - image: an image;
  - y: number of pixels to shift, 0;
  - x: number of pixels to shift, 0.

  Returns:
  - bsctrnsl: result image;
  '''  

  shiftX = step.get('x', 0)
  shiftY = step.get('y', 0)

  if shiftX == 0 and shiftY == 0:
    return kwargs

  M = np.float32([[1, 0, shiftX], [0, 1, shiftY]])
  kwargs['image'] = cv2.warpAffine(kwargs['image'], M, (kwargs['image'].shape[1], kwargs['image'].shape[0])) 

  return kwargs


@flowoperation
def fit(step, **kwargs):
  '''
  resize image1 regarding image

  Keyword arguments (key, default):
  - image: an image;
  - image1: an image.

  - meth - interpolation method, 2:
    - cv2.INTER_NEAREST - 0;
    - cv2.INTER_LINEAR - 1;
    - cv2.INTER_AREA - 2;
    - cv2.INTER_CUBIC - 3;
    - cv2.INTER_LANCZOS4 - 4;

  Returns:
  - bsctrnsl: result image;
  '''  

  method = step.get('meth', cv2.INTER_AREA)

  image = kwargs['image']
  (h, w, n) = image.shape
  image1 = kwargs['image1']
  (h1, w1, n1) = image1.shape
  
  if (h == h1 and w == w1):
    return kwargs

  dim = (w, h)

  kwargs['image'] = cv2.resize(image1, dim, interpolation=method) 

  return kwargs


@flowoperation
def transform(step, **kwargs):
  '''
  Transforms a skewed image to obtain a top-down view of the original image

  Keyword arguments (key, default):
  - image: an image;

  Returns:
  - result image;
  '''  

  rect_cnt = kwargs['rect']
	
  # warped = four_point_transform(image, rect_cnt.reshape(4, 2) * ratio) 
  kwargs['image'] = _four_point_transform(kwargs['image'], rect_cnt.reshape(4, 2)) 

  return kwargs


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