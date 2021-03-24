'''
Blob operations
'''
import cv2


def simple(step, **kwargs):
  '''
  Detects blobs.

  Keyword arguments:
  - image: an image;
  
  Step arguments (key, default):
  - mint - min threshold, 10;
  - maxt - max threshold, 200;
  - fltarea - filter by area, True;
  - minarea - min area, 1500;
  - fltcirc - filter by circularity, True;
  - mincirc - min circularity, 0.1;
  - fltconv - filter by convexity, True;
  - minconv - min convexity, 0.87;
  - fltiner - filter by inertia, True;
  - minciner - min inertia ratio, 0.01.
  
  Returns:
  - kpnts: blobs keypoints.
  '''

  minThreshold = step.get('mint', 10)
  maxThreshold = step.get('maxt', 200)
  filterByArea = step.get('fltarea', True)
  minArea = step.get('minarea', 1500)
  filterByCircularity = step.get('fltcirc', True)
  minCircularity = step.get('mincirc', 0.1)
  filterByConvexity = step.get('fltconv', True)
  minConvexity = step.get('minconv', 0.87)
  filterByInertia = step.get('fltiner', True)
  minInertiaRatio = step.get('minciner', 0.01)


  # Set up the detector with default parameters.
  detector = cv2.SimpleBlobDetector()
  
  # Setup SimpleBlobDetector parameters.
  params = cv2.SimpleBlobDetector_Params()

  # Change thresholds
  params.minThreshold = minThreshold;
  params.maxThreshold = maxThreshold;
  # Filter by Area.
  params.filterByArea = filterByArea
  params.minArea = minArea
  # Filter by Circularity
  params.filterByCircularity = filterByCircularity
  params.minCircularity = minCircularity
  # Filter by Convexity
  params.filterByConvexity = filterByConvexity
  params.minConvexity = minConvexity
  # Filter by Inertia
  params.filterByInertia = filterByInertia
  params.minInertiaRatio =   minInertiaRatio

  # Create a detector with the parameters
  detector = cv2.SimpleBlobDetector_create(params)

  # Detect blobs.
  kwargs['kpnts'] = detector.detect(kwargs['image'])

  return kwargs

