'''
  Contains common utility operations

  An operation docstring pattern:

  Parameters:
    - params:   
      name: type=default value; comment
    - data: 
      key: type; commnet
  Returns:
    - data:
      key: type; commnet

  Examples:
  1. Single parameter:
    name: int=0; integer parameter
    name: float=0; float parameter
    name: string=''; string parameter
  2. List of values:
    name: List[int](0,1,2,3)=2; list of integer values
  3. Dictionary:
    name: Dict[str,int](KEY1:0,KEY2:1,KEY3:3)=KEY2; dictionary of [str, int] pairs
  4. Range:
    name: Range[int](10,150,1)=50; range of integers from 10 to 150, default 50
'''

from typing import Dict
import cv2
import json
import PIL


def empty(params: Dict , **data: Dict) -> Dict:
  '''
  It is an operation's implementation boilerplate.

  Parameters:
    - params:   
    - data: 
  Returns:
    - data:
  '''  
  return data

def store(params: Dict , **data: Dict) -> Dict:
  '''
  Stores an image into a file.
  
  Parameters:
    - params:   
      path: str=; path to a folder with images
      name: str=; the image file name 
    - data: 
  Returns:
    - data:
      image: np.dtype; the stored image
  '''

  image = data.get('image')

  path = params.get('path', '')
  fn = params.get('name', '')
  
  ffn = '{}/{}'.format(path, fn)
  cv2.imwrite(ffn, image)
  return data


def restore(params: Dict , **data: Dict) -> Dict:
  '''
  Restores an image from a file.
  
  Parameters:
    - params:   
      load: bool=True; an imput image will be loaded
      path: str=; path to a folder with images
      name: str=; the image file name 
    - data: 
  Returns:
    - data:
      image: np.dtype; the loaded image
  '''

  path = params.get('path', '')
  fn = params.get('name', '')
  ffn = '{}/{}'.format(path, fn)
  data['image'] = cv2.imread(ffn)
  return data

def store_json(params: Dict , **data: Dict) -> Dict:
  '''
  Stores an json data into a file.
  
  Parameters:
    - params:   
      path: str=; path to a folder with images
      name: str=; the data file name 
    - data:
      json: str=; data for store
  Returns:
    - data:
  '''

  json_data = data.get('json')

  path = params.get('path', '')
  fn = params.get('name', '')
  
  ffn = '{}/{}'.format(path, fn)
  if fn is not '':
    with open(ffn, 'w') as fp:
      json.dump(json_data, fp, indent=2)
  return data

def restore_json(params: Dict , **data: Dict) -> Dict:
  '''
  Restores an json data from a file.
  
  Parameters:
    - params:   
      path: str=; path to a folder with images
      name: str=; the data file name 
    - data:
  Returns:
    - data:
      json: str=; restored data
  '''

  json_data = data.get('json')

  path = params.get('path', '')
  fn = params.get('name', '')
  
  ffn = '{}/{}'.format(path, fn)
  if fn is not '':
    with open(ffn, 'rt') as f:
      json_data = json.load(f)
  data['json'] = json_data
  return data
