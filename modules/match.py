import cv2
# Matching operations

# Brute-Force Matchers
def bfm_knn(**kwargs):
  '''
  matcher takes normType, which is set to 
  cv2.NORM_L1 for SIFT and SURF, 
  cv2.NORM_L2 for SIFT and SURF, 
  cv2.NORM_HAMMING for ORB, FAST, BRISK and BRIEF
  cv2.NORM_HAMMING2 for ORB if it uses VTA_K == 3 or 4
  '''
  type = kwargs.get('type', cv2.NORM_L2)
  cross_check = kwargs.get('check', True)
  k = kwargs.get('k', 2)
  descs_a = kwargs['da']
  descs_b = kwargs['db']

  bfm = cv2.BFMatcher(type, crossCheck=cross_check)
  matches = bfm.knnMatch(descs_a, descs_b, k=k)

  kwargs['matches'] = matches

  return kwargs


def bfm_knn(**kwargs):
  '''
  matcher takes normType, which is set to 
  cv2.NORM_L1 for SIFT and SURF, 
  cv2.NORM_L2 for SIFT and SURF, 
  cv2.NORM_HAMMING for ORB, FAST, BRISK and BRIEF
  cv2.NORM_HAMMING2 for ORB if it uses VTA_K == 3 or 4
  '''
  type = kwargs.get('type', cv2.NORM_L2)
  cross_check = kwargs.get('check', True)
  descs_a = kwargs['da']
  descs_b = kwargs['db']

  bfm = cv2.BFMatcher(type, crossCheck=cross_check)
  matches = bfm.Match(descs_a, descs_b)

  kwargs['matches'] = matches

  return kwargs