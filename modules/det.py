'''
Keypoin detection operations
'''
import cv2
from modules import flowoperation

@flowoperation
def fast(step, **kwargs):
  '''
  Detects keypoints using FAST  (Features from Accelerated Segment Test) algorithm.

  Keyword arguments (key, default):
  - image: an image;
  - thrs: threshold;
  - nonmax: non max suppression;
  - type: neighborhood type:
    - cv2.TYPE_5_8: 0,
    - cv2.TYPE_7_12: 1,
    - cv2.TYPE_9_16: 2

  Returns:
  - image;
  - kps: keypoints.
  '''   

  threshold = step.get('thrs', 25)
  nonmax_suppression = step.get('nonmax', True)
  type = step.get('type', 0)

  detector = cv2.FastFeatureDetector_create(threshold=threshold, nonmaxSuppression=nonmax_suppression, type=type)
  kps = detector.detect(kwargs['image'], None)
  kwargs['kps'] = kps

  return kwargs


@flowoperation
def star(step, **kwargs):
  '''
  Detects keypoints using STAR algorithm.

  Keyword arguments (key, default):
  - image: an image;

  Returns:
  - image;
  - kps: keypoints.
  '''

  max_size = step.get('max', 45)
  resp_threshold = step.get('resp-thrs', 30)
  proj_threshold = step.get('proj-thrs', 10)
  bin_threshold = step.get('binthrs', 8)
  nonmax_suppression_size = step.get('nonmax-size', 5)

  detector = cv2.xfeatures2d.StarDetector_create(max_size, resp_threshold, proj_threshold, bin_threshold, nonmax_suppression_size)  
  kps = detector.detect(kwargs['image'])
  kwargs['kps'] = kps

  return kwargs

# More detectors
# Harris Corner Detection
# Shi-Tomasi Corner Detector 
# SIFT
# SURF
# BRIEF (Binary Robust Independent Elementary Features)
# ORB (Oriented FAST and Rotated BRIEF)
# 
