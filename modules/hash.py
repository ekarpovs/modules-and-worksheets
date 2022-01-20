'''
Hashing operations
'''
from typing import Dict
from PIL import Image
import imagehash
import base64
import hashlib

def dhashm(params: Dict , **data: Dict) -> Dict:
  '''
  Computes the (relative) horizontal gradient between adjacent column pixels

  Parameters:
    - params:
    - data: 
      image: ndarray; an image
  Returns:
    - data:
      dhashm: float; diffeerence hash
  '''

  diff = data['image'][:, 1:] > data['image'][:, :-1]
	# convert the difference image to a hash
  dhash = sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])
  data['dhashm'] = dhash
  return data

def ahash(params: Dict , **data: Dict) -> Dict:
  '''
  Computes the average hash

  Parameters:
    - params:
    - data: 
      image: ndarray; an image
  Returns:
    - data:
      ahash: string; average hash
  '''

  image = data.get('image')
  hash = imagehash.average_hash(Image.fromarray(image))
  data['ahash'] = "{}".format(hash)
  return data

def dhash(params: Dict , **data: Dict) -> Dict:
  '''
  Computes the difference hash

  Parameters:
    - params:
    - data: 
      image: ndarray; an image
  Returns:
    - data:
      dhash: string; difference hash
  '''

  image = data.get('image')
  hash = imagehash.dhash(Image.fromarray(image))
  data['dhash'] = "{}".format(hash)
  return data

def phash(params: Dict , **data: Dict) -> Dict:
  '''
  Computes the perceptual hash

  Parameters:
    - params:
    - data: 
      image: ndarray; an image
  Returns:
    - data:
      phash: string; perceptual hash
  '''

  image = data.get('image')
  hash = imagehash.phash(Image.fromarray(image))
  data['phash'] = "{}".format(hash)
  return data

def whash(params: Dict , **data: Dict) -> Dict:
  '''
  Computes the wavelet hash

  Parameters:
    - params:
    - data: 
      image: ndarray; an image
  Returns:
    - data:
      whash: string; wavelet hash
  '''

  image = data.get('image')
  hash = imagehash.whash(Image.fromarray(image))
  data['whash'] = "{}".format(hash)
  return data

def clrhash(params: Dict , **data: Dict) -> Dict:
  '''
  Computes the color hash

  Parameters:
    - params:
    - data: 
      image: ndarray; an image
  Returns:
    - data:
      clrhash: string; color hash
  '''

  image = data.get('image')
  hash = imagehash.colorhash(Image.fromarray(image))
  data['clrhash'] = "{}".format(hash)
  return data

def md5hash(params: Dict , **data: Dict) -> Dict:
  '''
  Computes the md5 hash

  Parameters:
    - params:
    - data: 
      image: ndarray; an image
  Returns:
    - data:
      md5hash: string; md5 hash
  '''

  image = data.get('image')
  strim = base64.b64encode(image)
  hash = hashlib.md5("{}".format(strim).encode('utf-8')).hexdigest()
  data['md5hash'] = "{}".format(hash)
  return data

def join(params: Dict , **data: Dict) -> Dict:
  '''
  Joins hashes

  Parameters:
    - params:
    - data: 
      dhashm: string; dhashm
      ahash: string; dhashm
      dhash: string; dhashm
      phash: string; dhashm
      whash: string; dhashm
      md5hash: string; md5hash
      clrhash: string; colorhash
  Returns:
    - data:
      hash: Dict[str,str]; dictioanary of hashes
  '''

  dhashm = data.get('dhashm','')
  ahash = data.get('ahash','')
  dhash = data.get('dhash','')
  phash = data.get('phash','')
  whash = data.get('whash','')
  md5hash = data.get('md5hash','')
  clrhash = data.get('clrhash','')
  hash = {'dhashm': dhashm, 'ahash': ahash, 'dhash': dhash, 'phash': phash, 'whash': whash, 'md5hash': md5hash, 'clrhash': clrhash}
  data['hash'] = hash
  return data
