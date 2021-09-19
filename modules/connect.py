'''
Connected Component Labeling operations
'''
import cv2


def basic(params, **data):
  '''
  Applys apply connected component analysis to the thresholded image 

    parameters:
    - params: 
      --n;l;[4,8];4-- c: connectivity

    - data: 
        image - reference to the image
  
  returns:
    - data: 
        num - number of total components, that were detected;
        labels - a mask named labels has the same spatial dimensions as input thresh image;
        stats - statistics on each connected component, including the bounding box coordinates and area;
        centroids - (x, y) coordinates of each connected component.
'''   
  connectivity = int(params.get('c', 4))
  output = cv2.connectedComponentsWithStats(data.get('image'), connectivity, cv2.CV_32S)
  (num_labels, labels, stats, centroids) = output 
  data['num'] = num_labels 
  data['labels'] = labels 
  data['stats'] = stats 
  data['centroids'] = centroids 
  return data



# Need to check and correct !!!!!!!!!
def stats(params, **data):
  '''
  Iterates through labels and parses each one.

    parameters:
    - params: 
      --n;s;[];0-- num: number of total components, that were detected
      --n;l;[];0-- labels: a mask named labels has the same spatial dimensions as input thresh image
      --n;l;[];0-- stats: statistics on each connected component, including the bounding box coordinates and area
      --n;l;[];0-- centroids: (x, y) coordinates of each connected component
    - data: 
        image - reference to the image 
  returns:
    - data: 
      ???????????????
  '''   
  num_labels = int(params.get('num-labels', 0))
  labels = int(params.get('labels', None))
  stats = int(params.get('stats', None))
  centroids = int(params.get('centroids', 0))

  for i in range(0, num_labels): 
    # extract the connected component statistics and centroid for
    # the current label
    x = stats[i, cv2.CC_STAT_LEFT]
    y = stats[i, cv2.CC_STAT_TOP]
    w = stats[i, cv2.CC_STAT_WIDTH]
    h = stats[i, cv2.CC_STAT_HEIGHT]
    area = stats[i, cv2.CC_STAT_AREA]
    (cX, cY) = centroids[i]
  return data
