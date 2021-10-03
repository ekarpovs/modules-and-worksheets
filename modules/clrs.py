'''
Color spaces operations
'''
import cv2


def clrs_split(params, **data):  
  '''
  Splits a colored (BGR) image to separate colors.

  parameters:
    - params:   
    - data: 
      image - reference to an image that will be splitted
  returns:
    - data:
       b - reference to a blue channel
       g - reference to a green channel
       r - reference to a red channel
  '''  
  image = data.get('image') 
  if len(image.shape) < 3:
    # input - gray or binary
    return data
  (B, G, R) = cv2.split(image)
  data['b'] = B
  data['g'] = G
  data['r'] = R
  return data


def clrs_merge(params, **data):  
  '''
  Mergess  separate colors to colored (BGR) image.

  parameters:
    - params:   
    - data: 
       b - reference to a blue channel
       g - reference to a green channel
       r - reference to a red channel
  returns:
    - data:
      image - reference to the merged image
  '''
  b = data['b']
  g = data['g']
  r = data['r']
  image = cv2.merge(b, g, r)
  data['image'] = image
  return data


def bgrto(params, **data):  
  '''
  Converts a colored (BGR) image to another color space.

  parameters:
    - params:
      --n;d;[BGR2BGRA:0,BGR2RGB:4,BGR2GRAY:6,BGR2XYZ:32,BGR2YCrCb:36,BGR2HSV:40,BGR2LAB:44,BGR2Luv:50,BGR2HLS:52,BGR2YUV:82];BGR2GRAY-- type: new color space cv2.COLOR_(...)   
    - data: 
      image - reference to an image that will be converted
  returns:
    - data:
      image - reference to the image in the new color space
  '''  
  type = params.get('type', cv2.COLOR_BGR2GRAY)
  if len(data['image'].shape) < 3:
    # input - gray or binary
    return data
  data['image'] = cv2.cvtColor(data.get('image'), type)
  return data


def rgbto(params, **data):  
  '''
  Converts a colored (RGB) image to another color space.

  parameters:
    - params:
      --n;d;[RGB2BGRA:0,RGB2BGR:4,RGB2GRAY:7];RGB2BGR-- type: new color space cv2.COLOR_(...)   
      # --n;d;[RGB2BGRA:0,RGB2BGR:4,RGB2GRAY:6,BGR2XYZ:32,BGR2YCrCb:36,BGR2HSV:40,BGR2LAB:44,BGR2Luv:50,BGR2HLS:52,BGR2YUV:82];BGR2GRAY-- type: new color space cv2.COLOR_(...)   
    - data: 
      image - reference to an image that will be converted
  returns:
    - data:
      image - reference to the image in the new color space
  '''  
  type = params.get('type', cv2.COLOR_RGB2BGR)
  if len(data['image'].shape) < 3:
    # input - gray or binary
    return data
  data['image'] = cv2.cvtColor(data.get('image'), type)
  return data
