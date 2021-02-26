import cv2
# Blob operation

def simple(**kwargs):

  minThreshold = kwargs.get('mint', 10)
  maxThreshold = kwargs.get('maxt', 200)
  filterByArea = kwargs.get('fltarea', True)
  minArea = kwargs.get('minarea', 1500)
  filterByCircularity = kwargs.get('fltcirc', True)
  minCircularity = kwargs.get('mincirc', 0.1)
  filterByConvexity = kwargs.get('fltconv', True)
  minConvexity = kwargs.get('minconv', 0.87)
  filterByInertia = kwargs.get('fltiner', True)
  minInertiaRatio = kwargs.get('minciner', 0.01)


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
