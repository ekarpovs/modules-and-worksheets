'''
Feature extaction operations
'''
import cv2

def freak(**kwargs):
  '''
  Extract features for given keypoints using FREAK algorithm.

  Keyword arguments (key, default):
  - image: an image;
  - kps: keypoints.

  Returns:
  - image;
  - desc: feature descriptor.
  '''

  kps = kwargs['kps']
  extractor = cv2.xfeatures2d.FREAK_create()
  (kps, descs) = extractor.compute(kwargs['image'], kps)
  kwargs['descs'] = descs

  return kwargs


def brief(**kwargs):
  '''
  Extract features for given keypoints using BRIEF algorithm.

  Keyword arguments (key, default):
  - image: an image;
  - kps: keypoints.

  Returns:
  - image;
  - desc: feature descriptor.
  '''

  kps = kwargs['kps']
  extractor = cv2.xfeatures2d.FREAK_create()
  (kps, descs) = extractor.compute(kwargs['image'], kps)
  kwargs['descs'] = descs

  return kwargs