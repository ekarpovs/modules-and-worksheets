'''
Smoothing operation
'''
import cv2


def bilateral(params, **data):
  '''
  Applies bilateral filtering to the input image

  parameters:
    - params: 
      --n;s;[];11-- d: diameter of each pixel neighborhood that is used during filtering
      --n;l;[21,41,61];21--sc: filter sigma in the color space
      --n;l;[7,21,39];21-- ss: filter sigma in the coordinate space
    - data: 
        image - reference to the image
  returns:
    - data: 
        image - reference to the result image
  '''
  diameter = params.get('d', 11)
  sigmaColor = params.get('sc', 21)
  sigmaSpace = params.get('ss', 7)
  data['image'] = cv2.bilateralFilter(data.get('image'), diameter, sigmaColor, sigmaSpace) 
  return data
