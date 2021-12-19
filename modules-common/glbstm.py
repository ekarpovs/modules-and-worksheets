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
  image = data.get('image')

  store = params.get('store', False)
  
  if store:
    path = params.get('path', '')
    fn = params.get('name', '')
    ffn = '{}/{}'.format(path, fn)
    cv2.imwrite(ffn, image)
  return data
