'''
Connected Component Labeling operations
'''
import cv2


def basic(step, **kwargs):
  '''
  Applys apply connected component analysis to the thresholded image 

  Keyword arguments:
  - image: an image;

   Step arguments (--Type:Domain:[Possible Values]:Default-- name: description):
  --n;l;[4,8];4-- c: connectivity

  Returns:
  - image;
  - num: number of total components, that were detected;
  - labels: a mask named labels has the same spatial dimensions as input thresh image;
  - stats: statistics on each connected component, including the bounding box coordinates and area;
  - centroids: (x, y) coordinates of each connected component.
  '''   

  connectivity = int(step.get('c', 4))

  output = cv2.connectedComponentsWithStats(kwargs['image'], connectivity, cv2.CV_32S)
  (num_labels, labels, stats, centroids) = output 

  kwargs['num'] = num_labels 
  kwargs['labels'] = labels 
  kwargs['stats'] = stats 
  kwargs['centroids'] = centroids 

  return kwargs



def stats(step, **kwargs):
  '''
  Iterates through labels and parses each one.

  Keyword arguments (key, default):
  - image: an image;

  Step arguments (--Type:Domain:[Possible Values]:Default-- name: description):
  --n;s;[];0-- num: number of total components, that were detected
  --n;l;[];0-- labels: a mask named labels has the same spatial dimensions as input thresh image
  --n;l;[];0-- stats: statistics on each connected component, including the bounding box coordinates and area
  --n;l;[];0-- centroids: (x, y) coordinates of each connected component


  Returns:
  - image;
  '''   

  num_labels = int(step.get('num', 0))
  labels = int(step.get('labels', None))
  stats = int(step.get('stats', None))
  centroids = int(step.get('centroids', 0))

  for i in range(0, num_labels): 
    # extract the connected component statistics and centroid for
    # the current label
    x = stats[i, cv2.CC_STAT_LEFT]
    y = stats[i, cv2.CC_STAT_TOP]
    w = stats[i, cv2.CC_STAT_WIDTH]
    h = stats[i, cv2.CC_STAT_HEIGHT]
    area = stats[i, cv2.CC_STAT_AREA]
    (cX, cY) = centroids[i]

  return kwargs
