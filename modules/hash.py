'''
Hashing operations
  dhashm: Computes the (relative) horizontal gradient between adjacent column pixels
  ahash: Computes the average hash
  dhash: Computes the difference hash
  phash: Computes the perceptual hash
  whash: Computes the wavelet hash
  clrhash: Computes the color hash
  md5hash: Computes the md5 hash
  join: Joins hashes
  hammingdist: Calculates hamming distamce for haches
'''

from typing import Dict
from PIL import Image
import imagehash
import base64
import hashlib
import cv2 

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
      hashjoin: Dict[str,str]; dictioanary of hashes
  '''

  dhashm = data.get('dhashm','')
  ahash = data.get('ahash','')
  dhash = data.get('dhash','')
  phash = data.get('phash','')
  whash = data.get('whash','')
  md5hash = data.get('md5hash','')
  clrhash = data.get('clrhash','')
  hashjoin = {'hashjoin':{'dhashm': dhashm, 'ahash': ahash, 'dhash': dhash, 'phash': phash, 'whash': whash, 'md5hash': md5hash, 'clrhash': clrhash}}
  data['hashjoin'] = hashjoin
  return data
  
def hammingdist(params: Dict , **data: Dict) -> Dict:
  '''
  Calculates hamming distamce for haches

  Parameters:
    - params:
    - data: 
      hashjoin01: Dict[str,str]; dictioanary of hashes #1
      hashjoin02: Dict[str,str]; dictioanary of hashes #2
  Returns:
    - data:
      hummingdistance: Dict[str,str]; dictionary of hamming distances
  '''

  hashjoin01 = data.get('hashjoin01').get('hashjoin')
  hashjoin02 = data.get('hashjoin02').get('hashjoin')

  dhashm01 = hashjoin01.get('dhashm')
  ahash01 = hashjoin01.get('ahash')
  dhash01 = hashjoin01.get('dhash')
  phash01 = hashjoin01.get('phash')
  whash01 = hashjoin01.get('whash')
  md5hash01 = hashjoin01.get('md5hash')
  clrhash01 = hashjoin01.get('clrhash')

  dhashm02 = hashjoin02.get('dhashm')
  ahash02 = hashjoin02.get('ahash')
  dhash02 = hashjoin02.get('dhash')
  phash02 = hashjoin02.get('phash')
  whash02 = hashjoin02.get('whash')
  md5hash02 = hashjoin02.get('md5hash')
  clrhash02 = hashjoin02.get('clrhash')

  hdist = {}
  if dhashm01 != '' and dhashm02 != '':
    # dhashmdist = int(dhashm01, 16) - int(dhashm02, 16)
    dhashmdist = bin(int(dhashm01, 16) ^ int(dhashm02, 16)).count('1')
    hdist['dhashmdist'] = dhashmdist
  if ahash01 != '' and ahash02 != '':
    # ahashdist = int(ahash01, 16) - int(ahash02, 16)
    ahashdist = bin(int(ahash01, 16) ^ int(ahash02, 16)).count('1')
    hdist['ahashdist'] = ahashdist
  if dhash01 != '' and dhash02 != '':
    # dhashdist = int(dhash01, 16) - int(dhash02, 16)
    dhashdist = bin(int(dhash01, 16) ^ int(dhash02, 16)).count('1')
    hdist['dhashdist'] = dhashdist
  if phash01 != '' and phash02 != '':
    # phashdist = int(phash01, 16) - int(phash02, 16)
    phashdist = bin(int(phash01, 16) ^ int(phash02, 16)).count('1')
    hdist['phashdist'] = phashdist
  if whash01 != '' and whash02 != '':
    # whashdist = int(whash01, 16) - int(whash02, 16)
    whashdist = bin(int(whash01, 16) ^ int(whash02, 16)).count('1')
    hdist['whashdist'] = whashdist
  if md5hash01 != '' and md5hash02 != '':
    # md5hashdist = int(md5hash01, 16) - int(md5hash02, 16)
    md5hashdist = bin(int(md5hash01, 16) ^ int(md5hash02, 16)).count('1')
    hdist['md5hashdist'] = md5hashdist
  if clrhash01 != '' and clrhash02 != '':
    # clrhashdist = int(clrhash01, 16) - int(clrhash02, 16)
    clrhashdist = bin(int(clrhash01, 16) ^ int(clrhash02, 16)).count('1')
    hdist['clrhashdist'] = clrhashdist

  data['hummingdistance'] = {'hummingdistance': hdist}
  return data
