'''
Blob operations
'''
import cv2


def simple(step, **kwargs):
  '''
  Detects blobs.

  Keyword arguments:
  - image: an image;
  
  Step arguments (--Type:Domain:[Possible Values]:Default-- name: description):
  --n;r;[0,115,1];50-- mint: min threshold
  --n;r;[115,255,1];200-- maxt: max threshold
  --b;f;[False,True];True-- fltarea: filter by area
  --n;r;[100,5000,100];1500-- minarea: min area
  --b;f;[False,True];True-- fltcirc: filter by circularity
  --f;r;[0.1,0.9,0.01];0.1-- mincirc: min circularity
  --b;f;[False, True];True-- fltconv: filter by convexity
  --f;r;[0.10,0.99,0.01];0.87-- minconv: min convexity
  --b;f;[False,True];True-- fltiner: filter by inertia
  --f;r;[0.01,0.1,0.01];0.01-- mininer: min inertia ratio
  
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
  minInertiaRatio = step.get('mininer', 0.01)


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

