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
      loadfrom: button=From; path and name of a loaded file 
      path: str=; path to a folder with images
      name: str=; the image file name
      flag: Dict[str, int](UNGHANGED:-1,GRAYSCALE:0,COLOR:1)=COLOR; flag one from cv2.IMREAD_(...)
    - data: 
  Returns:
    - data:
      image: array[dtype[uint8]]; the loaded image
  '''

  path = params.get('path', '')
  fn = params.get('name', '')
  flag = params.get('flag', 1)

  if path is not '' and fn is not '':
    ffn = '{}/{}'.format(path, fn)
    data['image'] = cv2.imread(ffn, flag)
  return data

def end(params: Dict, **data: Dict) -> Dict:
  '''
  The last in a flow.

  Parameters:
    - params:   
      saveas: button=To; path and name of a stored file 
      path: str=; path to an output folder
      name: str=; the output file name 
    - data: 
      image: array[dtype[uint8]]; the stored image
  Returns:
    - data: 
  '''

  path = params.get('path', '')
  fn = params.get('name', '')
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
      image:array[dtype[uint8]]; the image
  Returns:
    - data:
      image:array[dtype[uint8]]; the image
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
    - data:
      image:array[dtype[uint8]]; the image
  Returns:
    - data:
      image:array[dtype[uint8]]; the image
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
      image:array[dtype[uint8]]; the image
  Returns:
    - data:
      image:array[dtype[uint8]]; the image
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
