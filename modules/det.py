'''
Keypoin detection operations
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
  data['kpnts'] = keypoints
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

# More detectors
# Harris Corner Detection
# Shi-Tomasi Corner Detector 
# SIFT
# SURF
# BRIEF (Binary Robust Independent Elementary Features)
# ORB (Oriented FAST and Rotated BRIEF)
# 
