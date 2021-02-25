import cv2
# Connected Component Labeling

def basic(**kwargs):
  """
  connectivity, type=int, default 4
  """

  connectivity = int(kwargs.get('c', 4))

  # apply connected component analysis to the thresholded image 
  output = cv2.connectedComponentsWithStats(kwargs['image'], connectivity, cv2.CV_32S)
  (num_labels, labels, stats, centroids) = output 

  kwargs['num'] = num_labels # number of total components, that were detected
  kwargs['labels'] = labels # A mask named labels has the same spatial dimensions as input thresh image.
  kwargs['stats'] = stats # Statistics on each connected component, including the bounding box coordinates and area
  kwargs['centroids'] = centroids # (x, y)-coordinates of each connected component

  return kwargs


def stats(**kwargs):
  """
  cv2.CC_STAT_LEFT 0
  cv2.CC_STAT_TOP 1
  cv2.CC_STAT_WIDTH 2
  cv2.CC_STAT_HEIGHT 3
  cv2.CC_STAT_AREA 4
  """

  num_labels = int(kwargs.get('num', 0))
  labels = int(kwargs.get('labels', None))
  stats = int(kwargs.get('stats', None))
  centroids = int(kwargs.get('centroids', 0))

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
