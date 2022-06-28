'''
Correlation operations (two images must to have the same dimension):

'''

from typing import Dict
import cv2
import numpy as np
import math as Math


def pearson(params: Dict, **data: Dict) -> Dict:
  '''
  Reshaps the images to two vectors, and then calculats the correlation coefficient
  This two images must to have the same dimension.

  Parameters:
    - params:
    - data: 
      image: ndarray; the first image
      scene: ndarray; the second image
  Returns:
    - data:
      correlation: Dict[str,float]; Correlation coefficient
  '''  

  image = data.get('image')
  scene = data.get('scene')
  image_1d = image.reshape(-1)
  scene_1d = scene.reshape(-1)
  corrcoef = np.corrcoef(image_1d, scene_1d)
  # Numpy implements a corrcoef() function that returns a matrix of correlations of:
  #  x with x, x with y, y with x and y with y. 
  # We're interested in the values of correlation of x with y 
  # (so position (1, 0) or (0, 1)).
  xx = corrcoef[0][0]
  xy = corrcoef[0][1]
  yx = corrcoef[1][0]
  yy = corrcoef[1][1]
  correlation = {'correlation': {'xx': xx, 'xy': xy, 'yx': yx, 'yy': yy}}
  data['correlation'] = correlation 
  return data

def phase(params: Dict, **data: Dict) -> Dict:
  '''
  Calculates the phase correlation between two images.

  https://stackoverflow.com/questions/57626656/interpreting-results-of-the-cv2-method-phasecorrelate-python-opencv
  Output like: ((4.3597901057868285, -2.8767423065464186), 0.4815432178477446)
  The first tuple returned tells you the amount of shift between img and img2 in x and y.
  The other values shows the response value that got from phase correlation process.

  Parameters:
    - params:
      trsh: int=4; detection threshold
    - data: 
      image: ndarray; the first gray image
      scene: ndarray; the second gray image
  Returns:
    - data:
      correlation: Dict[str,float]; Correlation coefficient
  '''

  trsh = params.get('trsh', 4)
  
  image = data.get('image')
  scene = data.get('scene')
  initial_frame = np.float32(image)
  current_frame = np.float32(scene)
  shift = cv2.phaseCorrelate(initial_frame, current_frame)
  radius = Math.hypot(shift[0][0], shift[0][1]) # Euclidean norm, sqrt(x*x + y*y).
  correlation = {'correlation': {'x': shift[0][0], 'y': shift[0][1], 'pc': shift[1]}, 'radius': radius}
  data['correlation'] = correlation 
  return data
