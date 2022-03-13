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

import cv2
import numpy as np
import json
import os
from typing import Dict


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
      dest: str=; the destination file name 
    - data: 
      image: ndarray; the stored image
  Returns:
    - data:
  '''

  image = data.get('image')

  path = params.get('path', '')
  fn = params.get('dest', '')
  
  ffn = '{}/{}'.format(path, fn)
  cv2.imwrite(ffn, image)
  return data

def restore(params: Dict , **data: Dict) -> Dict:
  '''
  Restores an image from a file.
  
  Parameters:
    - params:   
      path: str=; path to a folder with images
      src: str=; the source file name 
      flag: Dict[str,int](UNGHANGED:-1,GRAYSCALE:0,COLOR:1)=COLOR; flag one from cv2.IMREAD_(...)
    - data: 
  Returns:
    - data:
      image: ndarray; the loaded image
      shape: Dict[str, int]; the shape of the loaded image
      im-src: str; full file name from the image was loade
  '''

  path = params.get('path', '')
  fn = params.get('src', '')
  flag = params.get('flag', 1)
 
  ffn = '{}/{}'.format(path, fn)
  image = cv2.imread(ffn, flag)
  (h, w) = image.shape[:2]

  data['image'] = image
  data['shape'] = {'shape': {'h': h, 'w': w}}
  data['im-src'] = {'im-src':ffn}
  return data

def store_npy_float64(params: Dict , **data: Dict) -> Dict:
  '''
  Stores an numpy array into a file.
  
  Parameters:
    - params:   
      path: str=; path to a folder with file
      dest: str=; the destination file name 
    - data: 
      arr: ndarray; the stored file
  Returns:
    - data:
  '''

  arr = data.get('arr')

  path = params.get('path', '')
  fn = params.get('dest', '')
  
  ffn = '{}/{}'.format(path, fn)
  np.save(ffn, arr)
  return data

def restore_npy_float_64(params: Dict , **data: Dict) -> Dict:
  '''
  Restores an numpy array from a file.
  
  Parameters:
    - params:   
      path: str=; path to a folder with array
      src: str=; the source file name 
    - data: 
  Returns:
    - data:
      arr: ndarray; the loaded array
  '''

  path = params.get('path', '')
  fn = params.get('src', '')
  ffn = '{}/{}'.format(path, fn)
  data['arr'] = cv2.load(ffn)
  return data

def store_json(params: Dict , **data: Dict) -> Dict:
  '''
  Stores an json data into a file.
  
  Parameters:
    - params:   
      path: str=; path to a folder with images
      dest: str=; the destination file name 
    - data:
      json: str=; data for store
  Returns:
    - data:
  '''

  json_data = data.get('json')

  path = params.get('path', '')
  fn = params.get('dest', '')
  
  ffn = '{}/{}'.format(path, fn)
  if fn != '':
    with open(ffn, 'w') as fp:
      json.dump(json_data, fp, indent=2)
  return data

def restore_json(params: Dict , **data: Dict) -> Dict:
  '''
  Restores an json data from a file.
  
  Parameters:
    - params:   
      path: str=; path to a folder with images
      src: str=; the source file name 
    - data:
  Returns:
    - data:
      json: str; restored data
  '''

  json_data = data.get('json')

  path = params.get('path', '')
  fn = params.get('src', '')
  
  ffn = '{}/{}'.format(path, fn)
  if fn != '':
    with open(ffn, 'rt') as f:
      json_data = json.load(f)
  data['json'] = json_data
  return data

def join_json(params: Dict , **data: Dict) -> Dict:
  '''
  Join json files from a folder.

  Parameters:
    - params:   
      path: str=; path to files for join
    - data: 
  Returns:
    - data:
      joined: str; joined data
  '''

  path = params.get('path')
  joined_data = {}
  names = [f for f in os.listdir(path) if f.endswith('.json')]
  for fn in names:
    ffn = f'{path}/{fn}'
    with open(ffn, 'rt') as f:
      json_data = json.load(f)
      _, fn = os.path.split(ffn)
      joined_data[fn[:-5]] = json_data
  data['joined'] = joined_data
  return data

def selector(params: Dict , **data: Dict) -> Dict:
  '''
  Pass to the output one from input images

  Parameters:
    - params:
      selector: List[str](image1,image2,image3,image4,image5)=image1; the selected image
    - data: 
      image1: ndarray; the 1st image
      image2: ndarray; the 2nd image
      image3: ndarray; the 3d image
      image4: ndarray; the 4th image
      image5: ndarray; the 5th image
  Returns:
    - data:
      image: ndarray; the selected image
  '''
  
  selector = params.get('selector', 'image1')
  image = data.get(selector)
  data['image'] = image
  return data
  