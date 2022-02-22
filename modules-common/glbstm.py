'''
Local module, contains global staments descriptions
'''
import cv2
from typing import Dict


def begin(params: Dict, **data: Dict) -> Dict:
  '''
  The first in a flow.

  Parameters:
    - params:   
      path: str=; path to a folder with images
      src: str=; the source file name
      flag: Dict[str,int](UNGHANGED:-1,GRAYSCALE:0,COLOR:1)=COLOR; flag one from cv2.IMREAD_(...)
    - data: 
  Returns:
    - data:
      image: ndarray; the loaded image
      shape: Dict[str,int]; the shape of the loaded image
      im-src: str; full file name from the image was loaded
  '''

  path = params.get('path', '')
  fn = params.get('src', '')
  flag = params.get('flag', 1)

  if path != '' and fn != '':
    ffn = '{}/{}'.format(path, fn)
    image = cv2.imread(ffn, flag)
    (h, w) = image.shape[:2]
    data['image'] = image
    data['shape'] = {'shape': {'h': h, 'w': w}}
    data['im-src'] = {'im-src':ffn}
  return data

def end(params: Dict, **data: Dict) -> Dict:
  '''
  The last in a flow.

  Parameters:
    - params:   
      path: str=; path to an output folder
      dest: str=; the destination file name 
    - data: 
      image: ndarray; the stored image
  Returns:
    - data: 
  '''

  path = params.get('path', '')
  fn = params.get('dest', '')
  image = data.get('image')
  
  if fn != '':
    ffn = '{}/{}'.format(path, fn)
    cv2.imwrite(ffn, image)
  return data

def if_begin(params: Dict, **data: Dict) -> Dict:
  '''
  The if statement begin operation. 
  Syntax:
    val-a oper val-b[--and(or)--val-c oper val-d...]
    where operation one from:
      ==,!=,<,<=,>,>=

  Parameters:
    - params:   
      condition: str=a==b; the if condition 
    - data:
      image:ndarray; the image
  Returns:
    - data:
      image:ndarray; the image
      if-result: bool; result
  '''
     
  condition = params.get('condition', 'a==b')
  image = data.get('image')

  # Calculate the condition

  data['if-result'] = eval(condition)
  return data

def if_end(params: Dict, **data: Dict) -> Dict:
  '''
  The if statement end operation. 

  Parameters:
    - params:   
    - data:
      if-result: bool; result
  Returns:
    - data:
  '''
  
  data['if-result'] = False
  return data


def while_begin(params: Dict, **data: Dict) -> Dict:
  '''
  The while statement begin operation. 
  Syntax:
    val-a oper val-b[--and(or)--val-c oper val-d...]
    where operation one from:
      ==,!=,<,<=,>,>=

  Parameters:
    - params:   
      condition: str=a==b; the if condition 
      res: bool=True; for debug purpose only
    - data:
      image: ndarray; the image
  Returns:
    - data:
      image: ndarray; the image
      while-result: bool; result
  '''
  
  res = params.get('res', True)
  condition = params.get('condition', 'a==b')
  image = data.get('image')

  # Calculate the condition

  # data['while-result'] = eval(condition)
  data['while-result'] = res
  return data

def while_end(params: Dict, **data: Dict) -> Dict:
  '''
  The while statement end operation. 

  Parameters:
    - params:   
    - data:
  Returns:
    - data:
  '''

  data['while-result'] = False
  return data


def for_begin(params: Dict, **data: Dict) -> Dict:
  '''
  The for statement begin operation. 
  Syntax:
    val-a oper val-b[--and(or)--val-c oper val-d...]
    where operation one from:
      ==,!=,<,<=,>,>=

  Parameters:
    - params:   
      condition: str=a==b; the if condition 
      res: bool=True; temporary result
    - data:
      image:ndarray; the image
  Returns:
    - data:
      image:ndarray; the image
      for-result: bool; result
  '''
  
  res = params.get('res', True)
  condition = params.get('condition', 'a==b')
  image = data.get('image')

  # Calculate the condition

  # data['for-result'] = eval(condition)
  data['for-result'] = res
  return data

def for_end(params: Dict, **data: Dict) -> Dict:
  '''
  The for statement end operation. 

  Parameters:
    - params:   
    - data:
  Returns:
    - data:
  '''

  data['for-result'] = False
  return data
