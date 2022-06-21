'''
Local module, contains global staments descriptions
'''
import cv2
from typing import Dict
import json

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
  '''

  path = params.get('path', '')
  fn = params.get('src', '')
  flag = params.get('flag', 1)

  if path != '' and fn != '':
    ffn = '{}/{}'.format(path, fn)
    image = cv2.imread(ffn, flag)

    data['image'] = image
  return data

def end(params: Dict, **data: Dict) -> Dict:
  '''
  The last in a flow.

  Parameters:
    - params:   
    - data: 
  Returns:
    - data: 
  '''

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
  Returns:
    - data:
      while-result: bool; result
  '''
  
  res = params.get('res', True)
  condition = params.get('condition', 'a==b')
  execution_context = data.get('executioncontext', None)
  if execution_context is None or len(execution_context) == 0:
    execution_context = {}
  else:
    execution_context = json.loads(execution_context)

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
    for x in range(start, end, increment)
  Parameters:
    - params:   
      start: int=0; the x start value 
      end: int=1; the x end value
      increment: int=1; increment
      weight: int=1; unit's weight
    - data:
      executioncontext: Dict; the statement execution context
  Returns:
    - data:
      value: int; x*weight
      executioncontext: Dict; current value
  '''
   
  start = params.get('start', 0)
  end = params.get('end', 1)
  increment = params.get('incr', 1)
  weight = params.get('weight', 1)

  execution_context = data.get('executioncontext')
  if execution_context.get('init'):
    current = start
    execution_context['init'] = False
  else:
    current = execution_context.get('current', 0)
    current += increment

  result = current < (end - increment)
  execution_context['result'] = result
  execution_context['current'] = current
  data['executioncontext'] = execution_context
  data['value'] = weight*current
  if not result:
    current = start
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

  return data
