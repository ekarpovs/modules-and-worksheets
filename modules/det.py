import cv2
# Keypoin detection operations

def freak(**kwargs):
  '''
  cv2.TYPE_5_8 = 0,
  cv2.TYPE_7_12 = 1,
  cv2.TYPE_9_16 = 2
  '''

  threshold = kwargs.get('thrs', 25)
  nonmax_suppression = kwargs.get('nonmax', True)
  type = kwargs.get('type', 0)

  detector = cv2.FastFeatureDetector_create(threshold=threshold, nonmaxSuppression=nonmax_suppression, type=type)
  kps = detector.detect(kwargs['image'], None)
  kwargs['kps'] = kps

  return kwargs


def star(**kwargs):

  max_size = kwargs.get('max', 45)
  resp_threshold = kwargs.get('resp-thrs', 30)
  proj_threshold = kwargs.get('proj-thrs', 10)
  bin_threshold = kwargs.get('binthrs', 8)
  nonmax_suppression_size = kwargs.get('nonmax-size', 5)

  detector = cv2.xfeatures2d.StarDetector_create(max_size, resp_threshold, proj_threshold, bin_threshold, nonmax_suppression_size)  
  kps = detector.detect(kwargs['image'])
  kwargs['kps'] = kps

  return kwargs
