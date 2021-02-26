import cv2
# Hashing operations

def dhash(**kwargs):

  # compute the (relative) horizontal gradient between adjacent
  # column pixels
  diff = kwargs['dhash'][:, 1:] > kwargs['dhash'][:, :-1]
	# convert the difference image to a hash
  dhash = sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])
  kwargs['dhash'] = dhash

  return kwargs
