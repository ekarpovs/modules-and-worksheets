import cv2
# Feature extaction operations

def freak(**kwargs):

  kps = kwargs['kps']
  extractor = cv2.xfeatures2d.FREAK_create()
  (kps, descs) = extractor.compute(kwargs['image'], kps)
  kwargs['descs'] = descs

  return kwargs


def brief(**kwargs):

  kps = kwargs['kps']
  extractor = cv2.xfeatures2d.FREAK_create()
  (kps, descs) = extractor.compute(kwargs['image'], kps)
  kwargs['descs'] = descs

  return kwargs