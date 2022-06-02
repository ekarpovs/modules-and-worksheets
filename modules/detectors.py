'''
Corners and lines detectors
'''

import cv2
import numpy as np
from typing import Dict


def harris_rect(params: Dict , **data: Dict) -> Dict:
  '''
  Harris Corner Detector.

  Parameters:
    - params:   
      kernel: Scale[int](3,15,1,0)=7; kernel size
      apperture: Scale[int](3,15,1,0)=7; apperture size
      k: Scale[float](0.00,0.1,0.01,0)=0.04; koeff
      thresh: Scale[int](20,255,1,0)=200; corners threshold
      minx: int=0; x min value
      miny: int=0; y min value
      draw: bool=False; draw corners (debug purpose)
    - data: 
      image: ndarray; the gray image
  Returns:
    - data:
      image: ndarray; the gray image
      rectangle: ndarray; vertexes coordinates of the rectangle
  '''

  kernel = params.get('kernel', 7)
  apperture = params.get('apperture', 7)
  k = params.get('k', 2)
  thresh = params.get('thresh', 200)
  minx = params.get('minx', 0)
  miny = params.get('miny', 0)
  draw = params.get('draw', False)

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
  rect_coord = []
  # if len(approx) == 4:
  # vertex = ['tl', 'tr', 'bl', 'br']
  rect = approx
  rect = [v for v in rect if v[0][0] > minx and v[0][1] > miny]
  for i, v in enumerate(rect):
    rect_coord.append(v[0].tolist())
    if draw:
      cv2.circle(image, v[0], 10, (255), 2)

  # transform the rect to contour format
  # numpy.array([[1,1],[10,50],[50,50]] 
  cntr = np.array([v[0] for v in rect])

  data['image'] = image
  data['rectangle'] = rect_coord #{'rectangle': rect_coord}
  return data


def shitomasi(params: Dict , **data: Dict) -> Dict:
  '''
  Shi-Tomasi Corner Detector.

  Parameters:
    - params:   
      maxcorners: Scale[int](4,50,1,0)=10; maximum number of corners to return
      qualitylevel: float=0.01; the minimal accepted quality of image corners
      mindistance: int=200; minimum possible Euclidean distance between the returned corners
    - data: 
      image: ndarray; the gray image
  Returns:
    - data:
      image: ndarray; the gray image
      rectangle: Dict[str, List]; vertexes coordinates of the rectangle
  '''

  max_corners = params.get('maxcorners', 10)
  quality_level = params.get('qualitylevel', 0.01)
  min_distance = params.get('mindistance', 200)

  image = data.get('image')

  corners= cv2.goodFeaturesToTrack(image, max_corners, quality_level, min_distance, blockSize=3, useHarrisDetector=True, k=0.04)
  
# cv2.goodFeaturesToTrack(image, maxCorners, qualityLevel, minDistance, [,mask[,blockSize[,useHarrisDetector[,k]]]])
# image - Input 8-bit or floating-point 32-bit, single-channel image
# maxCorners - Maximum number of corners to return. If there are more corners than are found, the strongest of them is returned. if &lt;= 0 implies that no limit on the maximum is set and all detected corners are returned
# qualityLevel - Parameter characterizing the minimal accepted quality of image corners. See the above paragraph for explanation
# minDistance - Minimum possible Euclidean distance between the returned corners
# mask - Optional region of interest. If the image is not empty it specifies the region in which the corners are detected
# blockSize - Size of an average block for computing a derivative covariation matrix over each pixel neighborhood
# useHarrisDetector - whether to use Shi-Tomasi or Harris Corner
# k - Free parameter of the Harris detector

  # approximate the contour
  coord = np.array(corners)
  peri = cv2.arcLength(coord, True)
  approx = cv2.approxPolyDP(coord, 0.02 * peri, True)

  rect = approx
  rect_coord = {}
  rect = [v for v in rect if v[0][0] > 3 and v[0][1] > 95]
  for i, v in enumerate(rect):
    x, y = v[0].tolist()
    rect_coord[i] = [int(x), int(y)]
    cv2.circle(image, (int(x), int(y)), 10, (255), 2)


  # for item in corners:
  #   x, y = item.ravel()
  #   cv2.circle(image, (int(x),int(y)), 5, (255, 0, 0), -1) # 7, 0.05, 25; 5,(0,0,255),-1

  data['image'] = image
  data['rectangle'] = {'rectangle': rect_coord}
  return data


def hough_lines(params: Dict , **data: Dict) -> Dict:
  '''
  Probabilistic Hough Lines Detector.
  Takes only a random subset of points that is sufficient for line detection

  Parameters:
    - params:   
      distance: Scale[int](1,20,1,0)=1; distance resolution in pixels
      angle: Scale[int](90,180,30,0)=180; angle resolution in degrees
      thresh: Scale[int](20,255,1,0)=100; corners threshold
      minlength: int=100; min allowed length of line
      maxgap: int=10; max allowed gap between line for joining them
      draw: bool=False; draw corners (debug purpose)
    - data: 
      image: ndarray; the Canny edged image
  Returns:
    - data:
      image: ndarray; the Canny edged image
      lines: List[ndarray]; array of rho and theta values
  '''
  
  distance = params.get('distance', 1)
  thresh = params.get('thresh', 100)
  minlength = params.get('minlength', 100)
  maxgap = params.get('maxgap', 10)
  draw = params.get('draw', False)

  image = data.get('image')
 
  # Get an array of rho and theta values
  houg_lines = cv2.HoughLinesP(image, distance, np.pi/180, thresh, minlength, maxgap)
  lines = []
  # runs till rho and theta values are in the range of the 2d array
  for points in houg_lines:
    # extracted points nested in the list
    x1,y1,x2,y2 = points[0]
      # rho,theta = points[0]
      # a = np.cos(theta)
      # b = np.sin(theta)
      # x0 = a*rho
      # y0 = b*rho
      # # the rounded off value of (rcos(theta)-1000sin(theta))
      # x1 = int(x0 + 1000*(-b))
      # # the rounded off value of (rsin(theta)+1000cos(theta))
      # y1 = int(y0 + 1000*(a))
      # # the rounded off value of (rcos(theta)+1000sin(theta))
      # x2 = int(x0 - 1000*(-b))
      # # the rounded off value of (rsin(theta)-1000cos(theta))
      # y2 = int(y0 - 1000*(a))
    lines.append([(x1,y1),(x2,y2)])

    if draw:
      h, w = image.shape[:2]
      canvas = np.ones((h, w, 3), dtype = "uint8")*255
      cv2.line(canvas,(x1,y1),(x2,y2),(0,0,255),2)
      image = canvas

  data['image'] = image
  data['lines'] = lines
  return data
