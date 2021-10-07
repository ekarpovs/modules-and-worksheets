'''
Local binary patterns operations
'''
import cv2
import numpy as np
from skimage import feature 


def describe(params, **data):
  '''
  Computes the Local Binary Pattern representation of the image.

    parameters:
    - params: 
      --n;s;[];8-- nimpts: number of circularly symmetric neighbour set points;
      --n;s;[];1-- radius: radius of the LBP;
      --s;l;[default, ror, uniform, nri_uniform];uniform-- method: method to determine the pattern;

    - data: 
        image - reference to the image
  returns:
    - data: 
        image - reference to the result image
        lbp - 
  '''
  image = data.get('image')
  
  numpts = params.get('numpts', 8)
  radius = params.get('radius', 1)
  method = params.get('method', 'uniform')

  lbp = feature.local_binary_pattern(image, numpts, radius, method=method)

  data['lbp'] = lbp
  return data