'''
Hashing operations
'''
import cv2
from modules import flowoperation

@flowoperation
def dhashm(step, **kwargs):
  '''
  Computes the (relative) horizontal gradient between adjacent column pixels

  Keyword arguments (key, default):
  - image: an image;

  Returns:
  - image;
  - dhash: diffeerence hash.
  '''

  diff = kwargs['image'][:, 1:] > kwargs['image'][:, :-1]
	# convert the difference image to a hash
  dhash = sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])

  kwargs['dhash'] = dhash

  return kwargs
