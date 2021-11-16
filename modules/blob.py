'''
Blob operations
'''
from typing import Dict
import cv2


def simple(params: Dict , **data: Dict) -> Dict:
  '''
  Detects blobs.

  Parameters:
    - params:   
      mint: Range[int](0,115,1)=50; min threshold
      maxt: Range[int](115,255,1)=200; max threshold
      fltarea: bool=True; fltarea: filter by area
      minarea: Range[int](100,5000,1)=1500; min area
      fltcirc: bool=True; fltarea: filter by circularity
      mincircularity: Range[float](0.1,0.9,0.01)=0.1; min circularity
      fltconv: bool=True; fltarea: filter by convexity
      minconvexity: Range[float](0.10,0.99,0.01)=0.87; min convexity
      fltinertia: bool=True; fltarea: filter by inertia
      mininertia: Range[float](0.01,0.1,0.01)=0.01; min inertia
    - data: 
      image: np.dtype; the image
  Returns:
    - data:
      kpnts: list[List[int]]; blobs keypoints
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

