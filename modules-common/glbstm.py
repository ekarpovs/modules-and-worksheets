'''
Local module, contains global staments descriptions
'''
import cv2
from typing import Dict


def begin(params: Dict , **data: Dict) -> Dict:
  '''
  The first in a flow.

  Parameters:
    - params:   
      use: bool=True; the flow will to use an imput image
      path: str=../data/input; path to a folder with images
      name: str=; the image file name 
    - data: 
      image: np.dtype; the image is loaded by the client programm
  Returns:
    - data:
      image: np.dtype; the blured image
  '''

  load = params.get('load', True)
  if load:
    path = params.get('path', '../data/input')
    fn = params.get('name', '')
    ffn = '{}/{}'.format(path, fn)
    data['image'] = cv2.imread(ffn)
  return data


def end(params: Dict , **data: Dict) -> Dict:
  '''
  The last in a flow.

  Parameters:
    - params:   
    - data: 
  Returns:
    - data:
  '''
  
  return data
