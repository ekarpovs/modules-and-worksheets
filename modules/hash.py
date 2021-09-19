'''
Hashing operations
'''
import cv2


def dhashm(params, **data):
  '''
  Computes the (relative) horizontal gradient between adjacent column pixels

  parameters:
    - params: 
    - data: 
        image - reference to the image
  returns:
    - data: 
        dhash: diffeerence hash
  '''
  diff = data['image'][:, 1:] > data['image'][:, :-1]
	# convert the difference image to a hash
  dhash = sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])
  data['dhash'] = dhash
  return data
