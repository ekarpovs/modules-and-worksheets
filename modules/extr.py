'''
Feature descriptors (extractors) operations:
  - FREAK 
  - BriefDescriptorExtractor
  - LUCID - Locally Uniform Comparison Image Descriptor
  - LATCH - Learned Arrangements of Three Patch Codes
  - DAISY
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
  kps = data['kps']
  extractor = cv2.xfeatures2d.FREAK_create()
  (kps, descs) = extractor.compute(data['image'], kps)
  data['descs'] = descs
  return data



def brief(params, **data):
  '''
  Extract features for given keypoints using LUCID algorithm.

  parameters:
    - params: 
    - data: 
        image - reference to the image
        kps: keypoints.
  returns:
    - data: 
        descs - feature descriptors
  '''

  kps = data['kps']
  extractor = cv2.xfeatures2d.FREAK_create()
  (kps, descs) = extractor.compute(data['image'], kps)
  data['descs'] = descs
  return data


def lucid(params, **data):
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
  kps = data['kps']
  extractor = cv2.xfeatures2d.LUCID_create(lucid_kernel=1, blur_kernel=2)
  (kps, descs) = extractor.compute(data['image'], kps)
  data['descs'] = descs
  return data
