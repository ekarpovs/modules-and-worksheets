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
  --n:s:[0,4,6,32,36,40,44,50,52,82]:6-- type: new color space cv2.COLOR_(BGR2BGRA, BGR2RGB, BGR2GRAY, BGR2XYZ, BGR2YCrCb, BGR2HSV, BGR2LAB, BGR2Luv, BGR2HLS, BGR2YUV);


  Returns:
  - image: result image;
  '''  

  type = step.get('type', cv2.COLOR_BGR2GRAY)

  if len(kwargs['image'].shape) == 2:
    # input - gray
    return kwargs

  kwargs['image'] = cv2.cvtColor(kwargs['image'], type)
 
  return kwargs
