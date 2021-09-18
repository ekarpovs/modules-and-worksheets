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
      --str;s[];""-- ffn: full file name, where the image will be stored

    - data: - reference to an image that will be stored

  returns:
    - data: 
      - reference to the stored image
  '''  
  ffn = params.get('ffn', '')
  image = params.get('image')

  if image is not None:
    cv2.imwrite(ffn, image)
  return data


def restore(params, **data):
  '''
  Restores an image from a file.
  
  parameters:
    - params: 
      --str;s;[];--  ffn: full file name, where from the image will be restored.
      --str;s;[];image-- key:  name of a reference to the restored image
  
  returns:
    - data: 
      - reference to the restored image
  '''  
  ffn = params.get('ffn', '')
  key = params.get('key', 'image')

  if ffn != '':
    data[key] = cv2.imread(ffn)
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
  - data without removed items
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
    - the data as is
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

