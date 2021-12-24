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
      define: button=Define; path and name of an image 
      path: str=; path to a folder with images
      name: str=; the image file name 
    - data: 
  Returns:
    - data:
      image: array[dtype[uint8]]; the loaded image
  '''

  path = params.get('path', '')
  fn = params.get('name', '')
  if path is not '' and fn is not '':
    ffn = '{}/{}'.format(path, fn)
    data['image'] = cv2.imread(ffn)
  return data

def end(params: Dict, **data: Dict) -> Dict:
  '''
  The last in a flow.

  Parameters:
    - params:   
      define: button=Define; path and name of an image 
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
      res: bool=True; temporary result
    - data:
      image:array[dtype[uint8]]; the image
  Returns:
    - data:
      image:array[dtype[uint8]]; the image
      if-result: bool=; result
  '''
  res = params.get('res', True)
  
  def _eval(cond: str) -> bool:
    return res
    
  condition = params.get('condition', 'a==b')

  # Parse (maps?) a condition
  condition = condition.replace('-', ' ')

  # Get an condition data via links
  # Calculate the condition

  data['if-result'] = _eval(condition)
  return data

def if_end(params: Dict, **data: Dict) -> Dict:
  '''
  The if statement end operation. 

  Parameters:
    - params:   
    - data:
      image:array[dtype[uint8]]; the image
  Returns:
    - data:
      image:array[dtype[uint8]]; the image
  '''

  return data
