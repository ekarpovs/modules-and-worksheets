'''
Keypoin detection operations:
  - Harris Corner Detection
  - Shi-Tomasi Corner Detector 
  - MSER
  - FAST
  - AGAST
  - GFFT
  - SimpleBlobDetector
  - StarDetector
  - MSDDetector
'''
import cv2


def fast(params, **data):
  '''
  Detects keypoints using FAST  (Features from Accelerated Segment Test) algorithm.

  parameters:
    - params: 
      --n;s;[];25-- thrs: threshold
      --b;f;[True,False];True-- nonmax: non max suppression
      --n;l;[0,1,2];0-- type: neighborhood type cv2.TYPE_(5_8, 7_12, 9_16)
    - data: 
        image - reference to the image 
  returns:
    - data: 
        kpnts - keypoints
'''   
  threshold = params.get('thrs', 25)
  nonmax_suppression = params.get('nonmax', True)
  type = params.get('type', 0)
  detector = cv2.FastFeatureDetector_create(threshold=threshold, nonmaxSuppression=nonmax_suppression, type=type)
  keypoints = detector.detect(data['image'], None)
  data['kps'] = keypoints
  return data


def star(params, **data):
  '''
  Detects keypoints using STAR algorithm.

  parameters:
    - params: 
      --n;s;[];45-- max: max-size;
      --n;s;[];30-- resp-thrs: resp-thrs;
      --n;s;[];10-- proj-thrs: proj-thrs;
      --n;s;[];8-- bin-thrs: bin-thrs;
      --n;s;[];5-- nonmax: nonmax-size;
    - data: 
        image - reference to the image 
  returns:
    - data: 
        kpnts - keypoints
  '''
  max_size = params.get('max', 45)
  resp_threshold = params.get('resp-thrs', 30)
  proj_threshold = params.get('proj-thrs', 10)
  bin_threshold = params.get('bin-thrs', 8)
  nonmax_suppression_size = params.get('nonmax-size', 5)
  detector = cv2.xfeatures2d.StarDetector_create(max_size, resp_threshold, proj_threshold, bin_threshold, nonmax_suppression_size)  
  keypoints = detector.detect(data['image'])
  data['kpnts'] = keypoints
  return data

# BRIEF (Binary Robust Independent Elementary Features)
# ORB (Oriented FAST and Rotated BRIEF)

# nonfree:
# SIFT
# SURF
# 


# REMARK
# https://stackoverflow.com/questions/61946202/how-to-manually-set-keypoints-and-extract-features
# Use the compute method in the orb API. Something standard would be

# kp = orb.detect(img,None)
# kp, des = orb.compute(img, kp)

# But for your case, key points come from user input so use something like
# input_kp = # comes from user
# kp, des = orb.compute(img, input_kp)

# Make sure that the input keypoints match the format that the compute method is expecting. 
# You can create a key point from x, y values like this.
# key_points = [cv2.KeyPoint(x1, y1, 1), cv2.KeyPoint(x2, y2, 1)]
