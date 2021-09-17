'''
Local module, contains common utility operations
'''
import cv2

def empty(step, **kwargs):
  '''
  It is an operation's implementation boilerplate.

  @kwargs:
  - image: an image that will be processed

  Step arguments pattern:
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
      d (dict of key/values)    N1:V1,N2:V2,N3:V3...,Nn:Vn
      r (range,step)            Nmin,Nmax,Step
      f (flag)                  0,1 or True,False

  Returns:
  - the kwargs as is.
  '''  

  print("step", step)
  print("kwargs")
  [print(k, v) for k, v in kwargs.items() if k != "image" and k != 'orig']

  return kwargs


def store(step, **kwargs):
  '''
  Stores an image into a file.
  
  @kwargs:
  - image: an image that will be stored;
 
  @step:
  --str;s[];""-- ffn: full file name, where the image will be stored
  
  Returns:
  - the kwargs as is.
  '''  
  ffn = step.get('ffn', '')

  image = kwargs.get('image')
  if image is not None:
    cv2.imwrite(ffn, image)
  return kwargs


def restore(step, **kwargs):
  '''
  Restores an image from a file.
  
  @step:
  --str;s;[];""--  ffn: full file name, where from the image will be restored.
  --str;s;[];""-- index: suffix for new 'image' key - 'image+idx'
  
  Returns:
  - the image.
  '''  
  ffn = step.get('ffn', '')
  index = step.get('index', '')

  key = 'image' + index 
  print(key, ffn)
  if ffn != '':
    kwargs[key] = cv2.imread(ffn)
  else:
    kwargs[key] = kwargs['image']
  return kwargs


def clean_kwargs(step, **kwargs):
  '''
  Cleans kwargs dictionary from defined items.
  
  @step:
  --str;s;[];""-- keys: keys, separated by ';' , that will be removed from the kwargs

  Returns:
  - the kwargs without removed items
  '''  
  keys = step.get('keys')

  if keys is not None:
    for key in [k for k in kwargs if k in keys]: kwargs.pop(key, None)
  return kwargs


def print_kwargs(step, **kwargs):
  '''
  Prints kwargs.

  Returns:
  - the kwargs as is.
  '''
  [print(k, v) for k, v in kwargs.items() if k != "image" and k != "orig"] 
  return kwargs

