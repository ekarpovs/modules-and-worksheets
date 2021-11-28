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
      path: str=../data/input; path to a folder with images
      name: str=; the image file name 
    - data: 
  Returns:
    - data:
      image: np.dtype; the stored image
  '''

  image = data.get('image')

  path = params.get('path', '../data/output')
  fn = params.get('name', '')
  ffn = '{}/{}'.format(path, fn)
  data['image'] = cv2.write(ffn, image)
  return data


def restore(params: Dict , **data: Dict) -> Dict:
  '''
  Restores an image from a file.
  
  Parameters:
    - params:   
      load: bool=True; an imput image will be loaded
      path: str=../data/input; path to a folder with images
      name: str=; the image file name 
    - data: 
      image: np.dtype; the image, that was loaded by a client programm
  Returns:
    - data:
      image: np.dtype; the loaded image
  '''

  path = params.get('path', '../data/input')

  fn = params.get('name', '')
  ffn = '{}/{}'.format(path, fn)
  data['image'] = cv2.imread(ffn)
  return data

