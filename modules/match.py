'''
Matching operations
'''
import cv2




def bfm_knn(params, **data):
  '''
  Computes images semilaraty using Brute-Force Matchers.

  parameters:
    - params: 
      --n;d;[NORM_L1(SIFT&SURF):1,NORM_L2(SIFT&SURF):2,HAMMING( ORB&FAST&BRISK&BRIEF):3,HAMMING2(ORB if it uses VTA_K == 3 or 4):4];NORM_L2(SIFT&SURF)-- meth: interpolation method cv2.cv2.NORM_(...)
      --b;f;[False,True];True-- - check: cross check
      --n;s;[];2-- k: draw two match-lines for each keypoint
    - data: 
        image - reference to the image
        da - feature descriptor of the first image;
        db - feature descriptor of the second image;
  returns:
    - data: 
        matches: matches
  '''
  type = params.get('type', cv2.NORM_L2)
  cross_check = params.get('check', True)
  k = params.get('k', 2)
  descs_a = data.get('da')
  descs_b = data.get('db')
  bfm = cv2.BFMatcher(type, crossCheck=cross_check)
  matches = bfm.knnMatch(descs_a, descs_b, k=k)
  data['matches'] = matches
  return data


def bfm(params, **data):
  '''
  Computes images semilaraty using Brute-Force Matchers.

  parameters:
    - params: 
      --n;d;[NORM_L1(SIFT&SURF):1,NORM_L2(SIFT&SURF):2,HAMMING( ORB&FAST&BRISK&BRIEF):3,HAMMING2(ORB if it uses VTA_K == 3 or 4):4];NORM_L2(SIFT&SURF)-- meth: interpolation method cv2.cv2.NORM_(...)
      --b;f;[False,True];True-- - check: cross check
      --n;s;[];2-- k: draw two match-lines for each keypoint
    - data: 
        image - reference to the image
        da - feature descriptor of the first image;
        db - feature descriptor of the second image;
  returns:
    - data: 
        matches: matches
  '''
  type = params.get('type', cv2.NORM_L2)
  cross_check = params.get('check', True)
  descs_a = data.get('da')
  descs_b = data.get('db')
  bfm = cv2.BFMatcher(type, crossCheck=cross_check)
  matches = bfm.Match(descs_a, descs_b)
  # sort in ascending order
  matches = sorted(matches, key=lambda val: val.distance)
  data['matches'] = matches
  return data


def good(params, **data):
  '''
  Selects matches regarding predefined distance.

  parameters:
    - params: 
      --f;r;[0.0,1.0,0.1];0.5-- dist: max distance;
    - data: 
        image - reference to the image
         matches - matches;
  returns:
    - data: 
        matches - good matches (< distance)
  '''
  distance = params.get('dist', 0.5)
  matches = data.get('matches')
  good = [m for m in matches if m.distance < distance]
  data['matches'] = good
  return data

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