'''
Homography operations.
cv2::decomposeHomographyMat which allows to decompose the homography matrix to a set of
 rotations, 
 translations 
 and plane normals. 
'''


from typing import Dict
import cv2


def find(params: Dict , **data: Dict) -> Dict:
  '''
   Construts homograpy matrix

    Parameters:
    - params:   
      meth: Dict[str,int](LMEDS:4,RANSAC:8,RHO:16)=RANSAC; method used to compute a homography matrix
    - data: 
      image: array[dtype[uint8]]; the image
      src-pts: array[dtype[float64]]; image points
      dst-pts: array[dtype[float64]]; scene points
  Returns:
    - data:
    homography: array[dtype[float64]]; homograpy matrix
  '''

  image = data.get('image')
  src_pts = data.get('src-pts')
  dst_pts = data.get('dst-pts')

  meth = params.get('meth', cv2.RANSAC)

  (_, mat) = cv2.findHomography(src_pts, dst_pts, meth)

  data['homography'] = mat
  return data
