'''
Harris corners detector
'''

import cv2
import numpy as np
from typing import Dict


def harris(params: Dict , **data: Dict) -> Dict:
  '''
  Detect corners on an image.

  Parameters:
    - params:   
      kernel: Scale[int](3,15,1,0)=7; kernel size
      apperture: Scale[int](3,15,1,0)=7; apperture size
      k: Scale[float](0.00,0.1,0.01,0)=0.04; koeff 
      draw: bool=False; draw corners (debug purpose)
      thresh: Scale[int](20,255,1,0)=200; corners threshold
    - data: 
      image: ndarray; the gray image
  Returns:
    - data:
      corners: ndarray;
      coordinates: Dict[str, List];
  '''

  kernel = params.get('kernel', 7)
  apperture = params.get('apperture', 7)
  k = params.get('k', 2)
  draw = params.get('draw', False)
  thresh = params.get('thresh', 200)

  image = data.get('image')

  if(apperture % 2 == 0):
    apperture -= 1
  
  # Detecting corners
  corners = cv2.cornerHarris(image, kernel, apperture, k)
  # Normalizing
  corners_norm = np.empty(corners.shape, dtype=np.float32)
  cv2.normalize(corners, corners_norm, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
  corners_norm_scaled = cv2.convertScaleAbs(corners_norm)
  # Drawing a circle around corners
  coordinates = []
  for i in range(corners_norm.shape[0]):
    for j in range(corners_norm.shape[1]):
      if int(corners_norm[i,j]) > thresh:
        coordinates.append([j,i])
        # if draw:
        #   cv2.circle(corners_norm_scaled, (j,i), 10, (255), 2)

  # approximate the contour
  coord = np.array(coordinates)
  peri = cv2.arcLength(coord, True)
  approx = cv2.approxPolyDP(coord, 0.02 * peri, True)
  # if our approximated contour has four points, then we
  # can assume that we have found our screen
  rect_coord = {}
  # if len(approx) == 4:
  rect = approx
  for i, c in enumerate(rect):
    rect_coord[i] = c[0].tolist()
    if draw:
      cv2.circle(corners_norm_scaled, c[0], 10, (255), 2)

  data['corners'] = corners_norm_scaled
  data['coordinates'] = {'coordinates': rect_coord}
  return data


def goodfeature(params: Dict , **data: Dict) -> Dict:
  '''
  Detect corners on an image.

  Parameters:
    - params:   
      kernel: Scale[int](3,15,1,0)=7; kernel size
      apperture: Scale[int](3,15,1,0)=7; apperture size
      k: Scale[float](0.00,0.1,0.01,0)=0.04; koeff 
    - data: 
      image: ndarray; the gray image
  Returns:
    - data:
      corners: ndarray;
  '''

  kernel = params.get('kernel', 7)
  apperture = params.get('apperture', 7)
  k = params.get('k', 2)

  image = data.get('image')

  if(apperture % 2 == 0):
    apperture -= 1

  corners = cv2.cornerHarris(image, kernel, apperture, k)

  data['corners'] = corners
  return data
