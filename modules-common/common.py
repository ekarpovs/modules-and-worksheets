'''
Contains common utility operations

  A setup parameter pattern:
  --Type;Domain;[Possible Values];Default-- name: description

  Where:
    Type         
      n (number)   
      f (float)
      s (string)   
      b (boolean)  
      o (object)   
    Domain                    Possible values in the domain
      s (single value)          V
      l (list of values)        V1,V2,V3...,Vn
      d (dict of key/value)    K1:V1,K2:V2,K3:V3...,Kn:Vn
      r (range,step)            Nmin,Nmax,Step
      f (flag)                  0,1 or True,False
'''
import cv2
import PIL


def empty(params, **data):
  '''
  It is an operation's implementation boilerplate.

  parameters:
    - params: - dictionary of the operation setup parameters 
    - data: - dictionary of references to a data that will be processed
  returns:
    - data: - dictionary of references to a data that have been processed
  '''  
  return data


def store(params, **data):
  '''
  Stores an image into a file.
  
  parameters:
    - params: 
      --str;s;[];-- path: path, where the image will be stored
      --str;s;[];f1.jpg-- fn: file name
    - data: 
        image - reference to an image that will be stored
  returns:
    - data: 
      image - reference to the stored image
  '''  
  path = params.get('path', '.')
  fn = params.get('fn', '')
  ffn = '{}/{}'.format(path, fn)
  image = data.get('image')
  if image is not None:
    cv2.imwrite(ffn, image)
  return data


def restore(params, **data):
  '''
  Restores an image from a file.
  
  parameters:
    - params: 
      --str;s;[];-- path: path, where the image will be stored
      --str;s;[];-- fn: file name
      --str;s;[];image-- key:  name of a reference to the restored image
  data:
  returns:
    - data: 
        image - reference to the restored image
  '''  
  path = params.get('path', '')
  fn = params.get('fn', '')
  ffn = '{}/{}'.format(path, fn)
  key = params.get('key', 'image')
  if ffn != '':
    data[key] = cv2.imread(ffn)
  else:
    data[key] = data['image']
  return data


def store_pil(params, **data):
  '''
  Stores an image into a file.
  
  parameters:
    - params: 
      --str;s;[];-- path: path, where the image will be stored
      --str;s;[];f1.jpg-- fn: file name
    - data: 
        image - reference to an image that will be stored
  returns:
    - data: 
      image - reference to the stored image
  '''  
  path = params.get('path', '.')
  fn = params.get('fn', '')
  ffn = '{}/{}'.format(path, fn)
  image_pil = data.get('image-pil')
  if image_pil is not None:
    # cv2.imwrite('{}/{}'.format(path, fn), image)
    image_pil.save(ffn)    
  return data


def restore_pil(params, **data):
  '''
  Restores an image from a file.
  
  parameters:
    - params: 
      --str;s;[];-- path: path, where the image will be stored
      --str;s;[];f1.jpg-- fn: file name
      --str;s;[];image-- key:  name of a reference to the restored image
  data:
  returns:
    - data: 
        image - reference to the restored image
  '''  
  key = params.get('key', 'image-pil')
  path = params.get('path', '')
  fn = params.get('fn', '')
  ffn = '{}/{}'.format(path, fn)
  if ffn != '':
    # data[key] = cv2.imread(ffn)
    data[key] = PIL.Image.open(ffn).convert('RGB')
  else:
    data[key] = data['image']
  return data


def clean_data(params, **data):
  '''
  Cleans data dictionary from defined items.
  
  parameters:
    - params: 
      --str;s;[];-- keys: keys, separated by ',' , that will be removed from the data
    - data: - dictionary of references to a data that will be processed
  returns:
   - data: without removed items
  '''  
  keys = params.get('keys')
  if keys is not None:
    keys_list = keys.split(',')
    keys_list = [k.strip() for k in keys_list]
    if len(keys_list) > 0:
      keys_list = keys.split(',')
      for key in [k for k in data if k in keys_list]: data.pop(key, None)
  return data


def print_data(params, **data):
  '''
  Prints data.

  parameters:
    - params: 
      --b;f;[True, False];True-- keys-only: print only all data keys
      --str;s;[];image, orig-- keys: keys, separated by ',' , that will be not printed
    - data: - dictionary of references to a data that will be processed
  returns:
    - data: as is
  '''
  keys_only = params.get('keys-only', True)
  keys = params.get('keys', 'image, orig')
  if keys_only:
    [print(k) for k, v in data.items()] 
  else:
    keys_list = keys.split(',')
    keys_list = [k.strip() for k in keys_list]
    [print(k, v) for k, v in data.items() if k not in keys_list] 
  return data
