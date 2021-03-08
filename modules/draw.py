'''
Drawing Keypoints and Matches operation
'''
import cv2
import numpy as np

def keypoints(**kwargs):
  """
  cv2.DRAW_MATCHES_FLAGS_DEFAULT = 0
  cv2.DRAW_MATCHES_FLAGS_DRAW_OVER_OUTIMG = 1,
  cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS = 2,
  cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS = 4
  """

  flag = kwargs.get('flag', cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

  keypoints = kwargs['kpnts']

  cv2.drawKeypoints(kwargs['image'].copy(), keypoints, np.array([]), (0,0,255), flag)

  return kwargs

# https://docs.opencv.org/3.4/d4/d5d/group__features2d__draw.html
def matches(**kwargs):
  """
  cv2.DRAW_MATCHES_FLAGS_DEFAULT = 0
  cv2.DRAW_MATCHES_FLAGS_DRAW_OVER_OUTIMG = 1,
  cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS = 2,
  cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS = 4
  """

  flag = kwargs.get('flag', cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

  image = kwargs['image']
  keypoints = kwargs['keypoints']

  # outImg	=	cv.drawMatches(	img1, keypoints1, img2, keypoints2, matches1to2, outImg[, matchColor[, singlePointColor[, matchesMask[, flags]]]]	)
  
  return kwargs
