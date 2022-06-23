'''
Local module, contains global staments descriptions and implementations
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
      executioncontext: Dict; the statement execution context
  Returns:
    - data:
      executioncontext: Dict; current value
  '''
  
  result = params.get('res', True) # Debug purpose only!!!
  condition = params.get('condition', 'a==b')

  execution_context = data.get('executioncontext')
  if execution_context is None:
    execution_context = {}
    execution_context['init'] = True

  if execution_context.get('init'):
    execution_context['init'] = False
    # Initialize somevalue
  else:
    # Change somevalue
    pass

  # Calculate the condition
  # result = eval(condition)
  execution_context['result'] = result
  data['executioncontext'] = execution_context
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
  if execution_context is None:
    execution_context = {}
    execution_context['init'] = True
    
  if execution_context.get('init'):
    execution_context['init'] = False
    current = start
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
