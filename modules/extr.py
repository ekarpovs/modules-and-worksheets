'''
Feature extaction operations
'''
import cv2


def freak(params, **data):
  '''
  Extract features for given keypoints using FREAK algorithm.

  parameters:
    - params: 
    - data: 
        image - reference to the image
        kps: keypoints.
  returns:
    - data: 
        descs - feature descriptors
  '''
  kpts = data['ktps']
  extractor = cv2.xfeatures2d.FREAK_create()
  (kpts, descs) = extractor.compute(data['image'], kpts)
  data['descs'] = descs
  return data



def brief(params, **data):
  '''
  Extract features for given keypoints using BRIEF algorithm.

  parameters:
    - params: 
    - data: 
        image - reference to the image
        kps: keypoints.
  returns:
    - data: 
        descs - feature descriptors
  '''

  kpts = data['kpts']
  extractor = cv2.xfeatures2d.FREAK_create()
  (kpts, descs) = extractor.compute(data['image'], kpts)
  data['descs'] = descs
  return data