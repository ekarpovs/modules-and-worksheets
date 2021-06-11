'''
Local module, place 'image' from previous operation into kwargs with a new key
'''
import cv2

def comm_to_nkey(step, **kwargs):
  '''
  Add the kwargs['image']
  
  Keyword arguments:
  - image: an image that will be into 

  Step arguments (--Type;Domain;[Possible Values];Default-- name: description):
  --s;s;[];'image1'-- nkey: new key name


  Returns:
  - the kwargs with image value with new key.
  '''  

  nkey = step.get('nkey', 'image1')

  kwargs[nkey] = kwargs['image']

  return kwargs
