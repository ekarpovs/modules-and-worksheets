'''
Matching operations
'''
import cv2
from modules import flowoperation


def bfm_knn(step, **kwargs):
  '''
  Computes images semilaraty using Brute-Force Matchers.

  Keyword arguments:
  - image: an image;

  step arguments (key, default):
  - type: an normolazing type, cv2.NORM_L2:
    - cv2.NORM_L1 for SIFT and SURF; 
    - cv2.NORM_L2 for SIFT and SURF;
    - cv2.NORM_HAMMING for ORB, FAST, BRISK and BRIEF;
    - cv2.NORM_HAMMING2 for ORB if it uses VTA_K == 3 or 4;
  - check: cross check, True;
  - k:;
  - da: feature descriptor of the first image;
  - db: feature descriptor of the second image;

  Returns:
  - image: result image;
  - matches: .
  '''
 
  type = step.get('type', cv2.NORM_L2)
  cross_check = step.get('check', True)
  k = step.get('k', 2)
  descs_a = kwargs['da']
  descs_b = kwargs['db']

  bfm = cv2.BFMatcher(type, crossCheck=cross_check)
  matches = bfm.knnMatch(descs_a, descs_b, k=k)

  kwargs['matches'] = matches

  return kwargs


def bfm(step, **kwargs):
  '''
  Computes images semilaraty using Brute-Force Matchers.

  Keyword arguments:
  - image: an image;

  Step arguments (key, default):
  - type: an normolazing type, cv2.NORM_L2:
    - cv2.NORM_L1 for SIFT and SURF; 
    - cv2.NORM_L2 for SIFT and SURF;
    - cv2.NORM_HAMMING for ORB, FAST, BRISK and BRIEF;
    - cv2.NORM_HAMMING2 for ORB if it uses VTA_K == 3 or 4;
  - check: cross check, True;
  - da: feature descriptor of the first image;
  - db: feature descriptor of the second image;

  Returns:
  - image: result image;
  - matches: .
  '''

  type = step.get('type', cv2.NORM_L2)
  cross_check = step.get('check', True)
  descs_a = kwargs['da']
  descs_b = kwargs['db']

  bfm = cv2.BFMatcher(type, crossCheck=cross_check)
  matches = bfm.Match(descs_a, descs_b)

  # sort in ascending order
  matches = sorted(matches, key=lambda val: val.distance)

  kwargs['matches'] = matches

  return kwargs


def good(step, **kwargs):
  '''
  Select matches regarding predefined distance.

  Keyword arguments:
  - image: an image;
  - matches: matches;
 
  Step arguments (key, default):
  - dist: max distance, 0.5.

  Returns:
  - matches: good matches (< distance).
  '''

  distance = step.get('dist', 0.5)

  matches = kwargs['matches']

  good = [m for m in matches if m.distance < distance]
  
  kwargs['matches'] = good

  return kwargs

"""
		# flann matcher
		FLANN_INDEX_KDTREE = 0
		index_param = dict(algorithm = FLANN_INDEX_KDTREE, trees = 3)
		search_param = dict(checks = 100)		

		flann = cv2.FlannBasedMatcher(index_param, search_param)
		#d1, d2 = None, None
		
		# getting all matches using kNN
		matches = flann.knnMatch(d1, d2, k = 2)
"""