'''
Drawing Contours, Bounding boxes, Keypoints, Matches operation, etc.
'''
import cv2
import numpy as np

def contours(step, **kwargs):
  '''
  Draws contours.

  Keyword arguments:
  - image: an image;
  - cntrs: contours.

  Returns:
  - kwargs;
  '''
  image = kwargs.get('image')
  cntrs = kwargs.get('cntrs')
  clone = image
  # loop over the (unsorted) contours and draw them
  for (i, c) in enumerate(cntrs):
    # orig = draw_contour(image.copy(), c, i)   
    # compute the center of the contour area and draw a circle
    # representing the center
    M = cv2.moments(c)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    # draw the center of the contour on the image
    cv2.circle(clone, (cX, cY), 10, (0, 255, 0), -1) 
    # compute the area and the perimeter of the contour
    # area = cv2.contourArea(c)
    # perimeter = cv2.arcLength(c, True)
    # print("Contour #{} -- area: {:.2f}, perimeter: {:.2f}".format(i + 1, area, perimeter))
    # draw the contour on the image
    cv2.drawContours(clone, [c], -1, (0, 255, 0), 2) 
    # draw the countour number on the image
    cv2.putText(clone, "#{}".format(i + 1), (cX - 20, cY), cv2.FONT_HERSHEY_SIMPLEX,
      1.0, (255, 255, 255), 2) 

  return kwargs


def keypoints(step, **kwargs):
  """
  Draws keypoints.

  Keyword arguments:
  - image: an image;

  Step arguments (--Type:Domain:[Possible Values]:Default-- name: description):
  --n;d;[DEFAULT:0,DRAW_OVER_OUTIMG:1,NOT_DRAW_SINGLE_POINTS:2,DRAW_RICH_KEYPOINTS:4];DRAW_RICH_KEYPOINTS-- flags: flags cv2.DRAW_MATCHES_FLAGS_(...)

  Returns:
  - kwargs;
  """
  flags = step.get('flags', cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

  image = kwargs.get('image')
  clone = image.copy()
  keypoints = kwargs.get('kpnts')
  im_with_keypoints = cv2.drawKeypoints(clone, keypoints, np.array([]), (0,0,255), flags)
  kwargs['image'] = im_with_keypoints
  return kwargs


# https://docs.opencv.org/3.4/d4/d5d/group__features2d__draw.html
def matches(step, **kwargs):
  """
  Draws matches.

  Keyword arguments:
  - image: an image;

  Returns:
  - image;
  """
  image = kwargs.get('image')
  keypoints = kwargs.get('keypoints')

  # outImg	=	cv.drawMatches(	img1, keypoints1, img2, keypoints2, matches1to2, outImg[, matchColor[, singlePointColor[, matchesMask[, flags]]]]	) 
  return kwargs


