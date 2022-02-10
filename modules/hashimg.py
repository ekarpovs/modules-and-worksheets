'''
Hashing operations, based on cv2.img_hash methods
'''

from typing import Dict
import cv2 

def blockmean(params: Dict , **data: Dict) -> Dict:
  '''
  Computes the hash, based on blockmean

  Parameters:
    - params:
    - data: 
      image: ndarray; an image
  Returns:
    - data:
      blockmean: ndarray; blockmean hash
  '''
 
  image = data.get('image')
  hsh = cv2.img_hash.BlockMeanHash_create()
  hash = hsh.compute(image)
  # inthash=int.from_bytes(hash.tobytes(), byteorder='big', signed=False)
  data['blockmean'] = hash
  return data

def average(params: Dict , **data: Dict) -> Dict:
  '''
  Computes the average hash

  Parameters:
    - params:
    - data: 
      image: ndarray; an image
  Returns:
    - data:
      average: List[int]; average hash
  '''

  image = data.get('image')
  hsh = cv2.img_hash.AverageHash_create()
  hash = hsh.compute(image)
  # inthash=int.from_bytes(hash.tobytes(), byteorder='big', signed=False)
  data['average'] = hash
  return data

def colormoment(params: Dict , **data: Dict) -> Dict:
  '''
  Computes the hash, based on color moments

  Parameters:
    - params:
    - data: 
      image: ndarray; an image
  Returns:
    - data:
      colormoment: List[int]; colormoment hash
  '''

  image = data.get('image')
  hsh = cv2.img_hash.ColorMomentHash_create()
  hash = hsh.compute(image)
  # inthash=int.from_bytes(hash.tobytes(), byteorder='big', signed=False)
  data['colormoment'] = hash
  return data

def marrhidreth(params: Dict , **data: Dict) -> Dict:
  '''
  Computes the Marr-Hidreth Operator based hash

  Parameters:
    - params:
    - data: 
      image: ndarray; an image
  Returns:
    - data:
      marrhidreth: List[int]; marrhidreth hash
  '''

  image = data.get('image')
  hsh = cv2.img_hash.MarrHidrethtHash_create()
  hash = hsh.compute(image)
  # inthash=int.from_bytes(hash.tobytes(), byteorder='big', signed=False)
  data['marrhidreth'] = hash
  return data

def phash1(params: Dict , **data: Dict) -> Dict:
  '''
  Computes the phash

  Parameters:
    - params:
    - data: 
      image: ndarray; an image
  Returns:
    - data:
      phash1: List[int];  phash
  '''

  image = data.get('image')
  hsh = cv2.img_hash.PHash_create()
  hash = hsh.compute(image)
  # inthash=int.from_bytes(hash.tobytes(), byteorder='big', signed=False)
  data['phash1'] = hash
  return data

def radialvariance(params: Dict , **data: Dict) -> Dict:
  '''
  Computes hash, based on Radon transform

  Parameters:
    - params:
    - data: 
      image: ndarray; an image
  Returns:
    - data:
      radialvariance: List[int]; radialvariance hash
  '''

  image = data.get('image')
  hsh = cv2.img_hash.RadialVarianceHash_create()
  hash = hsh.compute(image)
  # inthash=int.from_bytes(hash.tobytes(), byteorder='big', signed=False)
  data['radialvariance'] = hash
  return data


def compare(params: Dict , **data: Dict) -> Dict:
  '''
  Compares two hashes.
  Value indicate similarity between inOne and inTwo, 
  the meaning of the value vary from algorithms to algorithms

  Parameters:
    - params:
    - data: 
      hashone: ndarray; hash one
      hashtwo: ndarray; hash two
  Returns:
    - data:
      sim: int; similarity between hashone and hashtwo
  '''

  hashone = data.get('hashone')
  hashtwo = data.get('hashtwo')
  
  # inthashone = int.from_bytes(hashone.tobytes(), byteorder='big', signed=False)
  # inthashtwo = int.from_bytes(hashtwo.tobytes(), byteorder='big', signed=False)

  sim = cv2.img_hash_ImgHashBase.compare(hashone, hashtwo)

  data['sim'] = sim
  return data

