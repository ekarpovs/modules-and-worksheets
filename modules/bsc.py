'''
Basic operations:
  crop: Crops an image
  crop_bound: Crops an image regarding roi coordinates and offsets
  flip: Flips an image
  resize: Resizes an image
  resize_abs: Resizes an image without aspect ratio (absolute resizing)
  rotate: Rotates an image without cropping
  rotate_inside: Rotates an input image with predefined bounding
  translate: Translates (Shifts) an image by a NumPy matrix in the form:
    [[1, 0, shiftX], [0, 1, shiftY]]
  fit: Resizes an input image regarding a scene image
  transform: Transforms a skewed image to obtain a top-down view of the original image
'''

import cv2
import numpy as np
from typing import Dict


def crop(params: Dict , **data: Dict) -> Dict:
  '''
  Crops an image.

  Parameters:
    - params:   
      y0: int=0; left top coordinate
      y1: int=0; left bottom coordinate
      x0: int=0; left top coordinate
      x1: int=0; right top coordinate
    - data: 
      image: ndarray; the image
  Returns:
    - data:
      image: ndarray; the result image
      coords: Dict[str, int]; the result image coordinates relatively to the input one - x0,y0,x1,y1
  '''  

  y0 = params.get('y0', 0)
  y1 = params.get('y1', 0)
  x0 = params.get('x0', 0)
  x1 = params.get('x1', 0)

  image = data.get('image')
  image = image[y0:y1, x0:x1]

  data['image'] = image
  data['coords'] = {'coords': {'x0': x0, 'y0': y0, 'x1': x1, 'y1': y1}}
  return data

def crop_bound(params: Dict , **data: Dict) -> Dict:
  '''
  Crops an image regarding roi coordinates and offsets.

  Parameters:
    - params:   
      y0: int=0; y top left corner
      off_top: int=0; y axis offset from top left corner
      x0: int=0; x top left corner
      off_left: int=0; x axis offset from left corner
      h: int=0; heigth of the cropped image
      w: int=0; width of the cropped image
    - data: 
      image: ndarray; the image
      coords: Dict[str,int]; coordinates - x0,y0,x1,y1
  Returns:
    - data:
      image: ndarray; the result image
      coords: Dict[str, int]; the result image coordinates relatively to the input one - x0,y0,x1,y1
  '''  

  y0 = params.get('y0', 0)
  x0 = params.get('x0', 0)
  off_top = params.get('off_top', 0)
  off_left = params.get('off_left', 0)
  h = params.get('h', 0)
  w = params.get('w', 0)

  image = data.get('image')
  coords = data.get('coords')

  if coords is not None:
    coords = coords.get('coords')
    y0 = coords.get('y0', 0) + off_top
    x0 = coords.get('x0', 0) + off_left
    
  image = image[y0:y0+h, x0:x0+w]

  data['image'] = image
  data['coords'] = {'coords': {'x0': x0, 'y0': y0, 'x1': x0+w, 'y1': y0+h}}
  return data

def flip(params: Dict , **data: Dict) -> Dict:
  '''
  Flips an image.

  Parameters:
    - params:   
      direct: Dict[str, int](both:0,vertical:1,horizontal:2)=vertical; flipping direction
    - data: 
      image: ndarray; the image
  Returns:
    - data:
      image: ndarray; the result image
  '''  

  direction = params.get('direct', 1)

  data['image'] = cv2.flip(data.get('image'), direction) 
  return data

def resize(params: Dict , **data: Dict) -> Dict:
  '''
  Resizes an image.

  Parameters:
    - params:   
      meth: Dict[str, int](NEAREST:0,LINEAR:1,AREA:2,CUBIC:3,LANCZOS:4)=AREA; interpolation method cv2.INTER_(...)
      unit: Dict[str, int](pixel:0,percent:1)=pixel; measurements unit
      side: Dict[str, int](height:0,width:1)=side; rectangle side
      size: int=20; new zise
    - data: 
      image: ndarray; the image
  Returns:
    - data:
      image: ndarray; the result image
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
    if side == 0:
      orig_pixels = h

    size = int((orig_pixels / 100) * size)
  
  #  the ratio of the new image to the old image, regarding to the side of a rectangle
  ratio = size / w
  dim = (size, int(h * ratio))
  if side == 0:
    ratio = size / h
    dim = (int(w * ratio), size)

  image = cv2.resize(image, dim, interpolation=method)

  data['image'] = image
  return data

def resize_abs(params: Dict , **data: Dict) -> Dict:
  '''
  Resizes an image without aspect ratio (absolute resizing).

  Parameters:
    - params:   
      meth: Dict[str, int](NEAREST:0,LINEAR:1,AREA:2,CUBIC:3,LANCZOS:4)=AREA; interpolation method cv2.INTER_(...)
      unit: Dict[str, int](pixel:0,percent:1)=pixel; measurements unit
      h: int=20; new height
      w: int=20; new width
    - data: 
      image: ndarray; the image
  Returns:
    - data:
      image: ndarray; the result image
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
    
  image = cv2.resize(image, dim, interpolation=method)

  data['image'] = image
  return data

def rotate(params: Dict , **data: Dict) -> Dict:  
  '''
  Rotates an image without cropping.
  
  Parameters:
    - params:   
      angle: Scale[int](0,180,1,0)=0; rotation angle
      neg: bool=True; negative direction
      smallangle: Scale[float](0.0,3.0,0.25,0)=0.0; small rotation angle
      usesmall: bool=False; use small angle scale
    - data:
      angle: int; 
      image: ndarray; the image
  Returns:
    - data:
      image: ndarray; the result image
      angle: int; rotation angle
  '''  

  # grab the dimensions of the image and calculate the center of the image
  image = data.get('image')
  (h, w) = image.shape[:2]
  (cx, cy) = (w / 2, h / 2)

  # calculate rotation matrix
  smallangle = params.get('smallangle', 0)
  usesmall = params.get('usesmall', False)
  angle = params.get('angle', 0)
  if 'angle' in data:
    dangle = data.get('angle')
    if dangle is not None:
      angle = int(dangle)
  if usesmall:
    angle = smallangle
  negative = params.get('neg', True)
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
  data['angle'] = {'angle': angle}
  return data

def rotate_inside(params: Dict , **data: Dict) -> Dict:  
  '''
  Rotates an input image with predefined bounding.
  
  Parameters:
    - params:   
      angle: Scale[float](0.0,3.0,0.25,0)=0.0; rotation angle
      neg: bool=True; negative direction
    - data: 
      image: ndarray; the image
      rect: ndarray; the canvas for result
  Returns:
    - data:
      image: ndarray; the result image
      angle: int; rotation angle
  '''  

  # grab the dimensions of the image and calculate the center of the image
  image = data.get('image')
  rect = data.get('rect')

  # calculate rotation matrix
  angle = params.get('angle', 0.0)
  negative = params.get('neg', True)
  if negative:
    angle *= -1
  
  (h, w) = image.shape[:2]
  (hr, wr) = rect.shape[:2]
  (cx, cy) = (wr / 2, hr / 2)

  # copy the image regarding the center of the canvas
  rect[int(cy - h/2): int(cy+h/2), int(cx - w/2): int(cx + w/2)] = image 

  M = cv2.getRotationMatrix2D((cx, cy), angle, 1.0)
  rotated = cv2.warpAffine(rect, M, (wr, hr), borderMode=cv2.BORDER_CONSTANT, borderValue=(255,255,255))

  data['image'] = rotated
  data['angle'] = {'angle': angle}
  return data

def translate(params: Dict , **data: Dict) -> Dict:
  '''
  Translates (Shifts) an image by a NumPy matrix in the form:
    [[1, 0, shiftX], [0, 1, shiftY]] .

  Parameters:
    - params:   
      y: int=0; number of pixels to shift
      x: int=0; number of pixels to shift
    - data: 
      image: ndarray; the image
  Returns:
    - data:
      image: ndarray; the result image
  '''

  shiftX = params.get('x', 0)
  shiftY = params.get('y', 0)

  if shiftX == 0 and shiftY == 0:
    return data

  image = data.get('image')
  M = np.float32([[1, 0, shiftX], [0, 1, shiftY]])
  data['image'] = cv2.warpAffine(image, M, (image.shape[1], image.shape[0])) 
  return data

def fit(params: Dict , **data: Dict) -> Dict:
  '''
  Resizes an input image regarding a scene image

  Parameters:
    - params:   
      meth: Dict[str, int](NEAREST:0,LINEAR:1,AREA:2,CUBIC:3,LANCZOS:4)=AREA; interpolation method cv2.INTER_(...)
    - data: 
      image: ndarray; the first image, that will be resized
      scene: ndarray; the second image
  Returns:
    - data:
      image: ndarray; the result image
  '''  

  method = params.get('meth', cv2.INTER_AREA)

  image = data.get('image')
  (h, w) = image.shape[:2]
  scene = data.get('scene')
  (h1, w1) = scene.shape[:2]
  if (h == h1 and w == w1):
    return data
  dim = (w1, h1)
  data['image'] = cv2.resize(image, dim, interpolation=method) 
  return data

def transform(params: Dict , **data: Dict) -> Dict:
  '''
  Transforms a skewed image to obtain a top-down view of the original image

  Parameters:
    - params:   
    - data: 
      image: ndarray; the image
      app-rect:  ndarray; the biggest rectangle contour 
  Returns:
    - data:
      image: ndarray; the result image
  '''  
  rect_cnt = data['app-rect']
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



  # angle *= 180/np.pi # convert to rad
  # Transformation matrix with a sequence of linear transformations (written in reverse order of application
  # M = cv2.TranslateBy((w-1)/2,(h-1)/2)*cv2.getRotationMatrix2D(angle)*cv2.TranslateBy(-cx, -cy)
  # T = cv2.getRotationMatrix2D((cx, cy), angle, 0.01)
  # print('T',T)
  # M =np.float32([[1,0.005,0], [-0.005,1,0]])
  # abs_cos = abs(M[0,0]) 
  # abs_sin = abs(M[0,1])
  # # find the new width and height bounds
  # bound_w = int(hr * abs_sin + wr * abs_cos)
  # bound_h = int(hr * abs_cos + wr * abs_sin)
  # # subtract old image center (bringing image back to original relative position) and adding the new image center coordinates
  # # M[0, 2] += bound_w/2 - cx
  # # M[1, 2] += bound_h/2 - cy
  # print(M, bound_w, bound_h)
  # rot_im = cv2.warpAffine(rot_im, M, (bound_w, bound_h))
  # x = int( cx - w/2  )
  # y = int( cy - h/2 )

    # #transformation matrix for Rotation
  # M = np.float32([[np.cos(angle_r), -(np.sin(angle_r)), 0],
  #               [np.sin(angle_r), np.cos(angle_r), 0],
  #               [0, 0, 1]])
  # apply a perspective transformation to the image
  # rot_im = cv2.warpPerspective(image, M, (wout, hout))

  # M =np.float32([[1, angle/180,10], [-angle/180,1,10]])
  # M = cv2.getRotationMatrix2D((cx, cy), angle, 1)
