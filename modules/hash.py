import cv2
# Hashing operations

def dhashm(**kwargs):

  # compute the (relative) horizontal gradient between adjacent
  # column pixels
  diff = kwargs['image'][:, 1:] > kwargs['image'][:, :-1]
	# convert the difference image to a hash
  dhash = sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])

  kwargs['dhash'] = dhash

  return kwargs
