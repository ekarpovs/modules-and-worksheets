'''
Local module, copies the kwargs[src-key] to kwargs[dst-key(s)]
'''
import cv2

def src_to_dst(params, **data):
  '''
  Copies the kwargs[src-key] to kwargs[dst-key(s)]
  
  parameters:
    - params: 
      --s;l;['image', 'image1', 'mask'];'image'-- src-key: src key name
      --s;l;['image', 'image1', 'mask'];'image'-- dst-key: src key name
    - data: 
        image - reference to the image
  returns:
    - data: 
        src-key - reference to the image
        dst-key - reference to the same image
  '''  
  src_key = params.get('src-key', 'image')
  dst_key = params.get('dst-key', 'image')
  data[dst_key] = data.get(src_key).copy()
  return data
