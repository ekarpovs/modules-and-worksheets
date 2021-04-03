'''
Local module, contains common utility operations
'''
import cv2

def empty(step, **kwargs):
  '''
  It is an operation's implementation boilerplate.

  Keyword arguments:
  - image: an image that will be returned

  Returns:
  - the kwargs as is.
  '''  

  print("step", step)
  print("kwargs")
  [print(k, v) for k, v in kwargs.items() if k != "image" and k != 'orig']

  return kwargs


def start(step, **kwargs):
  '''
  The always first operation in a flow.

  Keyword arguments:
  - None

  Step arguments:
  - ffn: full file name of the image will be processed.

  Returns:
  - orig - input image;
  - image - copy of the input image.
  '''  

  ffn = step.get('ffn', '')
  kwargs['orig'] = cv2.imread(ffn)
  kwargs['image'] = kwargs['orig']

  return kwargs


def store(step, **kwargs):
  '''
  Stores an image into a file.
  
  Keyword arguments:
  - image: an image that will be stored;
 
  Step arguments:
  - ffn: full file name, where the image will be stored.
  
  Returns:
  - the kwargs as is.
  '''  

  
  ffn = step.get('ffn', '')
  print("store", ffn)

  image = kwargs['image']


  if image is not None:
    cv2.imwrite(ffn, image)

  return kwargs


def restore(step, **kwargs):
  '''
  Restores an image from a file.
  
  Step arguments:
  - ffn: full file name, where from the image will be restored.
  
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


def clean(step, **kwargs):
  '''
  Cleans kwargs dictionary from items.
  
  Keyword arguments:
  - image: an image that will be returned

  Returns:
  - the kwargs with only 'exec', 'image', 'brk' and 'show' items.
  '''  

  const_keys = ['exec', 'image', 'orig']
  for key in [k for k in kwargs if k not in const_keys]: kwargs.pop(key, None)

  return kwargs


def printkwargs(step, **kwargs):
  '''
  Prints kwargs.

  Keyword arguments:
  - image: an image that will be returned

  Returns:
  - the kwargs as is.
  '''

  [print(k, v) for k, v in kwargs.items() if k != "image" and k != "orig"]
  
  return kwargs

