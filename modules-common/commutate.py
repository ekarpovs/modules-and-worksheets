'''
Local module, copies the kwargs[src-key] to kwargs[dst-key(s)]
'''
import cv2

def src_to_dst(step, **kwargs):
  '''
  Copies the kwargs[src-key] to kwargs[dst-key(s)]
  
  Keyword arguments:
  - image: an image that will be into 

  Step arguments (--Type;Domain;[Possible Values];Default-- name: description):
  --s;l;['image', 'image1', 'mask'];'image'-- src-key: src key name
  --s;l;['image', 'image1', 'mask'];'image'-- dst-key: src key name

  Returns:
  - the kwargs with src and its copy(es).
  '''  

  src_key = step.get('src-key', 'image')
  dst_key = step.get('dst-key', 'image')

  kwargs[dst_key] = kwargs.get(src_key).copy()

  return kwargs
