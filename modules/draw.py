'''
Drawing Contours, Bounding boxes, Keypoints, Matches operation, etc.
'''
import cv2
import numpy as np

def contours(params, **data):
  '''
  Draws contours.

  parameters:
    - params: 
    - data: 
      image - reference to the image
      cntrs - contours
  returns:
    - data: 
  '''
  image = data.get('image')
  cntrs = data.get('cntrs')
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
  return data


def keypoints(params, **data):
  """
  Draws keypoints.

  parameters:
    - params: 
      --n;d;[DEFAULT:0,DRAW_OVER_OUTIMG:1,NOT_DRAW_SINGLE_POINTS:2,DRAW_RICH_KEYPOINTS:4];DRAW_RICH_KEYPOINTS-- flags: flags cv2.DRAW_MATCHES_FLAGS_(...)
    - data: 
      image - reference to the image
      kpnts - keypoints
  returns:
    - data: 
        image - reference to the image with the keypoints
  """
  flags = params.get('flags', cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

  image = data.get('image')
  clone = image.copy()
  keypoints = data.get('kpnts')
  im_with_keypoints = cv2.drawKeypoints(clone, keypoints, np.array([]), (0,0,255), flags)
  data['image'] = im_with_keypoints
  return data


# https://docs.opencv.org/3.4/d4/d5d/group__features2d__draw.html
def matches(params, **data):
  """
  Draws matches.

  parameters:
    - params: 
      --str;s;[];image1--  key: name of a reference to the second image
    - data: 
        image - reference to the first image
        key - reference to the second image
        kpnts - keypoints
  returns:
    - data: 
        image - reference to the image with the matches
  """
  key = params.get('key', 'image1')
  first = data.get('image')
  second = data.get(key)
  keypoints = data.get('kpnts')

  # outImg	=	cv.drawMatches(	img1, keypoints1, img2, keypoints2, matches1to2, outImg[, matchColor[, singlePointColor[, matchesMask[, flags]]]]	) 
  return data


