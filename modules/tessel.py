
'''
Compare operations
'''

from typing import Dict
import numpy as np

def square(params: Dict, **data: Dict) -> Dict:
  '''
  Define tessel for an image.

  Parameters:
    - params:
      cells: int=0; number of cells 
      rows: int=0; number of rows 
    - data: 
      image: ndarray; the first image
  Returns:
    - data:
      image: ndarray; the first image
      tessel: List[Dict]; tessel for the image
  '''  

  cells = params.get('cells', 0)
  rows = params.get('rows', 0)

  image = data.get('image')
  h, w = image.shape[:2]
  tessel = []
   
  data['image'] = image
  data['tessel'] = tessel
  return data

  def _gcd(a: int, b: int) -> int:
    '''
    Calculate the Greatest Common Divisor of a and b.
    '''

    if a%b == 0:
        return b
    return gcd(b, a%b)    