'''
Color spaces operations
'''
import cv2


def bgrto(step, **kwargs):  
  '''
  Converts a colored (BGR) image to another color space.

  Keyword arguments:
  - image: an image;
  
  Step arguments (--Type:Domain:[Possible Values]:Default-- name: description):
  --n;d;[BGR2BGRA:0,BGR2RGB:4,BGR2GRAY:6,BGR2XYZ:32,BGR2YCrCb:36,BGR2HSV:40,BGR2LAB:44,BGR2Luv:50,BGR2HLS:52,BGR2YUV:82];BGR2GRAY-- type: new color space cv2.COLOR_(...)


  Returns:
  - image: result image;
  '''  

  type = step.get('type', cv2.COLOR_BGR2GRAY)

  if len(kwargs['image'].shape) == 2:
    # input - gray
    return kwargs

  kwargs['image'] = cv2.cvtColor(kwargs['image'], type)
 
  return kwargs
