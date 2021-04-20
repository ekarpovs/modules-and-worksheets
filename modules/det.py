'''
Keypoin detection operations
'''
import cv2


def fast(step, **kwargs):
  '''
  Detects keypoints using FAST  (Features from Accelerated Segment Test) algorithm.

  Keyword arguments:
  - image: an image;

  Step arguments (--Type:Domain:[Possible Values]:Default-- name: description):
  --n:v:[]:25-- thrs: threshold;
  --b:v:[True,False]:True-- nonmax: non max suppression;
  --n:s:[0,1,2]:0-- type: neighborhood type cv2.TYPE_(5_8, 7_12, 9_16);

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



def star(step, **kwargs):
  '''
  Detects keypoints using STAR algorithm.

  Keyword arguments (key, default):
  - image: an image;
  
  Step arguments (key, default):
  - resp-thrs:
  - proj-thrs:
  - binthrs:
  - nonmax-size:

  Step arguments (--Type:Domain:[Possible Values]:Default-- name: description):
  --n:v:[]:45-- max: max-size;
  --n:v:[]:30-- resp-thrs: resp-thrs;
  --n:v:[]:10-- proj-thrs: proj-thrs;
  --n:v:[]:8-- bin-thrs: bin-thrs;
  --n:v:[]:5-- nonmax: nonmax-size;

  Returns:
  - image;
  - kps: keypoints.
  '''

  max_size = step.get('max', 45)
  resp_threshold = step.get('resp-thrs', 30)
  proj_threshold = step.get('proj-thrs', 10)
  bin_threshold = step.get('bin-thrs', 8)
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
