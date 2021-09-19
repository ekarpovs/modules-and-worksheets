'''
Blob operations
'''
import cv2


def simple(params, **data):
  '''
  Detects blobs.

  parameters:
    - params:
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
    - data: 
      image - reference to an source image
  returns:
    - data:
      - kpnts: blobs keypoints.
  '''
  minThreshold = params.get('mint', 10)
  maxThreshold = params.get('maxt', 200)
  filterByArea = params.get('fltarea', True)
  minArea = params.get('minarea', 1500)
  filterByCircularity = params.get('fltcirc', True)
  minCircularity = params.get('mincirc', 0.1)
  filterByConvexity = params.get('fltconv', True)
  minConvexity = params.get('minconv', 0.87)
  filterByInertia = params.get('fltiner', True)
  minInertiaRatio = params.get('mininer', 0.01)
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
  data['kpnts'] = detector.detect(data['image'])
  return data

