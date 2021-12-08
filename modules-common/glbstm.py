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
      image: np.dtype; the image, that was loaded by a client programm
  Returns:
    - data:
      image: np.dtype; the loaded image
  '''

  load = params.get('load', True)
  if load:
    path = params.get('path', '')
    fn = params.get('name', '')
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
  Returns:
    - data: 
      image: np.dtype=None; image
  '''
  image = data.get('image')

  store = params.get('store', False)
  
  if store:
    path = params.get('path', '')
    fn = params.get('name', '')
    ffn = '{}/{}'.format(path, fn)
    cv2.imwrite(ffn, image)
  return data
