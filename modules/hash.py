'''
Hashing operations
'''
from typing import Dict
import cv2


def dhashm(params: Dict , **data: Dict) -> Dict:
  '''
  Computes the (relative) horizontal gradient between adjacent column pixels

  Parameters:
    - params:
    - data: 
      image: np.dtype; an image
  Returns:
    - data:
      dhash: float; diffeerence hash
  '''

  diff = data['image'][:, 1:] > data['image'][:, :-1]
	# convert the difference image to a hash
  dhash = sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])
  data['dhash'] = dhash
  return data
