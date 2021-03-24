# WorkSheet: ./modules
## Module: ws-aux
Local module, contains common utility operations

### Function: empty
  It is an operation's implementation boilerplate.

  Keyword arguments:
  - image: an image that will be returned

  Returns:
  - the kwargs as is.
  

### Function: store
  Stores an image into a file.
  
  Keyword arguments:
  - image: an image that will be stored;
 
  Step arguments:
  - ffn: full file name, where the image will be stored.
  
  Returns:
  - the kwargs as is.
  

### Function: restore
  Restores an image from a file.
  
  Step arguments:
  - ffn: full file name, where from the image will be restored.
  
  Returns:
  - the image.
  

### Function: clean
  Cleans kwargs dictionary from items.
  
  Keyword arguments:
  - image: an image that will be returned

  Returns:
  - the kwargs with only 'exec', 'image', 'brk' and 'show' items.
  

### Function: printkwargs
  Prints kwargs.

  Keyword arguments:
  - image: an image that will be returned

  Returns:
  - the kwargs as is.
  

# WorkSheet: ../../modules-and-worksheets/modules
## Module: bitwise
Bitwise operations

### Function: btw_and
  Performs AND operation.

  Keyword arguments:
  - image: the first image;
  - image1: the second image.
  
  Returns:
  - image: result image;
  

### Function: btw_or
  Performs OR operation.

  Keyword arguments:
  - image: the first image;
  - image1: the second image.
  
  Returns:
  - image: result image;
  

### Function: btw_xor
  Performs XOR operation.

  Keyword arguments:
  - image: the first image;
  - image1: the second image.
  
  Returns:
  - image: result image;
  

### Function: btw_not
  Performs NOT operation.

  Keyword arguments:
  - image: the first image;
  - image1: the second image.
  
  Returns:
  - image: result image;
  

## Module: blob
Blob operations

### Function: simple
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
  

## Module: blur
Bluring operation

### Function: avg
  Performs average bluring.

  Keyword arguments:
  - image: an image;

  Step arguments (key, default):
  - k: kernel size, 3.
  
  Returns:
  - image: result image;
  

### Function: gaus
  Performs gausian bluring.

  Keyword arguments:
  - image: an image;

  Step arguments (key, default):
  - k: kernel size, 3.
  
  Returns:
  - image: result image;
  

### Function: median
  Performs median bluring.

  Keyword arguments:
  - image: an image;

  Step arguments (key, default):
  - k: kernel size, 3.
  
  Returns:
  - image: result image;
  

## Module: bsc
Basic operations

### Function: crop
  Crops an image.

  Keyword arguments:
  - image: an image;

  Step arguments (key, default):
  - y0 - left top coordinate, 0;
  - y1 - left right coordinate, h;
  - x0 - left top coordinate, 0;
  - x1 - left right coordinate, w.
  
  Returns:
  - image: result image;
  

### Function: flip
  Flipss an image.

  Keyword arguments:
  - image: an image;

  Step arguments (key, default):
  - drct: direction, 1.
 
  Returns:
  - image: result image;
  

### Function: mask
  Applys a mask to an image.

  Keyword arguments:
  - image: an image;

  Step arguments (key, default):
  - type - the mask shape (rectangle 0, circle 1) , 1;

    for rectangle:
    - y0 - left top coordinate, 0;
    - y1 - left right coordinate, h;
    - x0 - left top coordinate, 0;
    - x1 - left right coordinate, w.

    for circle:
    - cx - Center coordinate, w/2;
    - cy - Center coordinate, h/2;
    - rad - the mask radius,min(h / 2, w /2).
 
  Returns:
  - image: result image;
  

### Function: resize
  Resizes an image.

  Keyword arguments:
  - image: an image;
  
  Step arguments (key, default):
  - meth - interpolation method, 2:
    - cv2.INTER_NEAREST - 0;
    - cv2.INTER_LINEAR - 1;
    - cv2.INTER_AREA - 2;
    - cv2.INTER_CUBIC - 3;
    - cv2.INTER_LANCZOS4 - 4;
  - unit - measurements unit, 0:
    - pixel - 0;
    - percent - 1;
  - side - rectangle side, 0:
    - height 0
    - width 1
 
  Returns:
  - image: result image;
  

### Function: resize1
  Resizes an image without aspect ratio (absolute resizing).

  Keyword arguments:
  - image: an image;
  
  Step arguments (key, default):
  - meth - interpolation method, 2:
    - cv2.INTER_NEAREST - 0;
    - cv2.INTER_LINEAR - 1;
    - cv2.INTER_AREA - 2;
    - cv2.INTER_CUBIC - 3;
    - cv2.INTER_LANCZOS4 - 4;
  - unit - measurements unit, 0:
    - pixel - 0;
    - percent - 1;
  - side - rectangle side, 0:
    - height 0
    - width 1
 
  Returns:
  - image: result image;
  

### Function: rotate
  Rotates an image without cropping.
  
  Keyword arguments:
  - image: an image;

  Step arguments (key, default):
  - angle: rotation angle, 0.

  Returns:
  - image: result image;
  

### Function: translate
  Translates (Shifts) an image by a NumPy matrix in the form:
    [[1, 0, shiftX], [0, 1, shiftY]] .

  Keyword arguments:
  - image: an image;

  Step arguments (key, default):
  - y: number of pixels to shift, 0;
  - x: number of pixels to shift, 0.

  Returns:
  - image: result image;
  

### Function: fit
  resize image1 regarding image

  Keyword arguments (key, default):
  - image: an image;
  - image1: an image.

  Step arguments (key, default):
  - meth - interpolation method, 2:
    - cv2.INTER_NEAREST - 0;
    - cv2.INTER_LINEAR - 1;
    - cv2.INTER_AREA - 2;
    - cv2.INTER_CUBIC - 3;
    - cv2.INTER_LANCZOS4 - 4;

  Returns:
  - image: result image;
  

### Function: transform
  Transforms a skewed image to obtain a top-down view of the original image

  Keyword arguments (key, default):
  - image: an image;

  Returns:
  -image: result image;
  

## Module: clrs
Color spaces operations

### Function: bgrto
  Converts a colored (BGR) image to another color space.

  Keyword arguments:
  - image: an image;
  
  Step arguments (key, default):
  - type - new color space:
    - cv2.COLOR_BGR2BGRA - 0;
    - cv2.COLOR_BGR2RGB - 4;
    - cv2.COLOR_BGR2GRAY - 6;
    - cv2.COLOR_BGR2XYZ - 32;
    - cv2.COLOR_BGR2YCrCb - 36;
    - cv2.COLOR_BGR2HSV - 40;
    - cv2.COLOR_BGR2LAB - 44;
    - cv2.COLOR_BGR2Luv - 50;
    - cv2.COLOR_BGR2HLS - 52;
    - cv2.COLOR_BGR2YUV - 82;
 
  Returns:
  - image: result image;
  

## Module: cmp
Compare operations

### Function: compare_ssim
    Compute the mean structural similarity index between two images.

    Parameters
    ----------
    im1, im2 : ndarray
        Images. Any dimensionality with same shape.
    win_size : int or None, optional
        The side-length of the sliding window used in comparison. Must be an
        odd value. If `gaussian_weights` is True, this is ignored and the
        window size will depend on `sigma`.
    gradient : bool, optional
        If True, also return the gradient with respect to im2.
    data_range : float, optional
        The data range of the input image (distance between minimum and
        maximum possible values). By default, this is estimated from the image
        data-type.
    multichannel : bool, optional
        If True, treat the last dimension of the array as channels. Similarity
        calculations are done independently for each channel then averaged.
    gaussian_weights : bool, optional
        If True, each patch has its mean and variance spatially weighted by a
        normalized Gaussian kernel of width sigma=1.5.
    full : bool, optional
        If True, also return the full structural similarity image.

    Other Parameters
    ----------------
    use_sample_covariance : bool
        If True, normalize covariances by N-1 rather than, N where N is the
        number of pixels within the sliding window.
    K1 : float
        Algorithm parameter, K1 (small constant, see [1]_).
    K2 : float
        Algorithm parameter, K2 (small constant, see [1]_).
    sigma : float
        Standard deviation for the Gaussian when `gaussian_weights` is True.

    Returns
    -------
    mssim : float
        The mean structural similarity index over the image.
    grad : ndarray
        The gradient of the structural similarity between im1 and im2 [2]_.
        This is only returned if `gradient` is set to True.
    S : ndarray
        The full SSIM image.  This is only returned if `full` is set to True.

    Notes
    -----
    To match the implementation of Wang et. al. [1]_, set `gaussian_weights`
    to True, `sigma` to 1.5, and `use_sample_covariance` to False.

    .. versionchanged:: 0.16
        This function was renamed from ``skimage.measure.compare_ssim`` to
        ``skimage.metrics.structural_similarity``.

    References
    ----------
    .. [1] Wang, Z., Bovik, A. C., Sheikh, H. R., & Simoncelli, E. P.
       (2004). Image quality assessment: From error visibility to
       structural similarity. IEEE Transactions on Image Processing,
       13, 600-612.
       https://ece.uwaterloo.ca/~z70wang/publications/ssim.pdf,
       :DOI:`10.1109/TIP.2003.819861`

    .. [2] Avanaki, A. N. (2009). Exact global histogram specification
       optimized for structural similarity. Optical Review, 16, 613-621.
       :arxiv:`0901.0065`
       :DOI:`10.1007/s10043-009-0119-z`

    

    Warns
    -----
    Deprecated:
        .. versionadded:: 0.16

        This function is deprecated and will be
        removed in scikit-image 0.18. Please use the function named
        ``structural_similarity`` from the ``metrics`` module instead.


    See also
    --------
    skimage.metrics.structural_similarity
    

### Function: cmp_mse
  Calculates 'Mean Squared Error' between pixels of two images.
  The 'Mean Squared Error' between the two images is the
  sum of the squared difference between the two images.
  This two images must have the same dimension.

  Keyword arguments (key, default):
  - image: an original image;
  - image1: an image to compare;

  Returns:
  - images;
  - mse: Mean Squared Errors.
  

### Function: cmp_ssim
  Calculates 'Structural Similarity Index' between pixels of two images.
  Uses to compare two windows instead an entire images.
  This two images must have the same dimension.

  Keyword arguments (key, default):
  - image: an original image;
  - image1: an image to compare;

  Returns:
  - images;
  - ssim: Structural Similarity Index.
  

### Function: cmp_psnr
  Calculates 'Peak Signal-to-Noise Ratio' between two images.
  This two images must have the same dimension.

  Keyword arguments (key, default):
  - image: an original image;
  - image1: an image to compare;

  Returns:
  - images;
  - psnr: Peak Signal-to-Noise Ratio.
  

### Function: cmp_norm
  Calculates 'Pixels difference' between two GRAY images.
  This two images must have the same dimension.

  Keyword arguments (key, default):
  - image: an original image;
  - image1: an image to compare;

  Returns:
  - images;
  - psnr: Difference.
  

## Module: cntrs
Contours operations

### Function: find
  Finds contours of an image.

  Keyword arguments:
  - image: an image;

  Step arguments (key, default):
  - mth: approximation method, 2:
    - cv2.CHAIN_APPROX_NONE: 1
    - cv2.CHAIN_APPROX_SIMPLE: 2
    - cv2.CHAIN_APPROX_TC89_L1: 3
    - cv2.CHAIN_APPROX_TC89_KCOS: 4
  - md: result mode, 0:
    - cv2.RETR_EXTERNAL: 0
    - cv2.RETR_LIST: 1
    - cv2.RETR_CCOMP: 2
    - cv2.RETR_TREE: 3
    - cv2.RETR_FLOODFILL: 4
  
  Returns:
  - image;
  - cntrs: list of the contours.
  

### Function: sort
  Sorts contours.

  Keyword arguments:
  - image: an image;
  - cntrs: contours;
 
   Step arguments (key, default):
   - rev: reverse flag, False;

  Returns:
  - image;
  - cntrs: list of the sorted contours.
  

### Function: sel_rect
  Sorts contours.

  Keyword arguments:
  - image: an image;
  - cntrs: sorted contours;

  Returns:
  - image;
  - rect: the biggest rectangle contour.
  

## Module: connect
Connected Component Labeling operations

### Function: basic
  Applys apply connected component analysis to the thresholded image 

  Keyword arguments:
  - image: an image;

  Step arguments (key, default):
  - c: connectivity, 4;
  
  Returns:
  - image;
  - num: number of total components, that were detected;
  - labels: a mask named labels has the same spatial dimensions as input thresh image;
  - stats: statistics on each connected component, including the bounding box coordinates and area;
  - centroids: (x, y) coordinates of each connected component.
  

### Function: stats
  Iterates through labels and parses each one.

  Keyword arguments (key, default):
  - image: an image;
  - num: number of total components, that were detected;
  - labels: a mask named labels has the same spatial dimensions as input thresh image;
  - stats: statistics on each connected component, including the bounding box coordinates and area;
  - centroids: (x, y) coordinates of each connected component.

  Returns:
  - image;
  

## Module: det
Keypoin detection operations

### Function: fast
  Detects keypoints using FAST  (Features from Accelerated Segment Test) algorithm.

  Keyword arguments:
  - image: an image;

  Step arguments (key, default):
  - thrs: threshold;
  - nonmax: non max suppression;
  - type: neighborhood type:
    - cv2.TYPE_5_8: 0,
    - cv2.TYPE_7_12: 1,
    - cv2.TYPE_9_16: 2

  Returns:
  - image;
  - kps: keypoints.
  

### Function: star
  Detects keypoints using STAR algorithm.

  Keyword arguments (key, default):
  - image: an image;
  
  Step arguments (key, default):
  - resp-thrs:
  - proj-thrs:
  - binthrs:
  - nonmax-size:

  Returns:
  - image;
  - kps: keypoints.
  

## Module: draw
Drawing Contours, Bounding boxes, Keypoints, Matches operation, etc.

### Function: contours
  Draws contours.

  Keyword arguments:
  - image: an image;
  - cntrs: contours.

  Returns:
  - image;
  

### Function: keypoints
  Draws keypoints.

  Keyword arguments:
  - image: an image;

  Step arguments (key, default):
  - flags: 4
    - cv2.DRAW_MATCHES_FLAGS_DEFAULT: 0
    - cv2.DRAW_MATCHES_FLAGS_DRAW_OVER_OUTIMG: 1,
    - cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS: 2,
    - cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS: 4

  Returns:
  - image;
  

### Function: matches
  Draws keypoints.

  Keyword arguments:
  - image: an image;

  Returns:
  - image;
  

## Module: edge
Gradient and edge dectection operations
Gradient magnitude and orientation.

### Function: sobel
  Computes compute gradients along the X or Y axis uses Sobel algorithm.

  Keyword arguments:
  - image: an image;

  Step arguments (key, default):
  - direction: 
    - x: 0
    - y: 1 

  Returns:
  - image: result image;
  

### Function: canny
  Computes a "wide", "mid-range", and "tight" threshold for the edges.

  Keyword arguments:
  - image: an image;

  Step arguments (key, default):
  - thrs1: threshold1;
  - thrs2: threshold2;

  Returns:
  - image: result image;
  

### Function: laplacian
  Computes the Laplacian of the image .

  Keyword arguments:
  - image: an image;

  Returns:
  - edgelap: result image;
  

## Module: extr
Feature extaction operations

### Function: freak
  Extract features for given keypoints using FREAK algorithm.

  Keyword arguments (key, default):
  - image: an image;
  - kps: keypoints.

  Returns:
  - image;
  - descs: feature descriptor.
  

### Function: brief
  Extract features for given keypoints using BRIEF algorithm.

  Keyword arguments (key, default):
  - image: an image;
  - kps: keypoints.

  Returns:
  - image;
  - descs: feature descriptor.
  

## Module: hash
Hashing operations

### Function: dhashm
  Computes the (relative) horizontal gradient between adjacent column pixels

  Keyword arguments (key, default):
  - image: an image;

  Returns:
  - image;
  - dhash: diffeerence hash.
  

## Module: match
Matching operations

### Function: bfm_knn
  Computes images semilaraty using Brute-Force Matchers.

  Keyword arguments:
  - image: an image;

  step arguments (key, default):
  - type: an normolazing type, cv2.NORM_L2:
    - cv2.NORM_L1 for SIFT and SURF; 
    - cv2.NORM_L2 for SIFT and SURF;
    - cv2.NORM_HAMMING for ORB, FAST, BRISK and BRIEF;
    - cv2.NORM_HAMMING2 for ORB if it uses VTA_K == 3 or 4;
  - check: cross check, True;
  - k:;
  - da: feature descriptor of the first image;
  - db: feature descriptor of the second image;

  Returns:
  - image: result image;
  - matches: .
  

### Function: bfm
  Computes images semilaraty using Brute-Force Matchers.

  Keyword arguments:
  - image: an image;

  Step arguments (key, default):
  - type: an normolazing type, cv2.NORM_L2:
    - cv2.NORM_L1 for SIFT and SURF; 
    - cv2.NORM_L2 for SIFT and SURF;
    - cv2.NORM_HAMMING for ORB, FAST, BRISK and BRIEF;
    - cv2.NORM_HAMMING2 for ORB if it uses VTA_K == 3 or 4;
  - check: cross check, True;
  - da: feature descriptor of the first image;
  - db: feature descriptor of the second image;

  Returns:
  - image: result image;
  - matches: .
  

### Function: good
  Select matches regarding predefined distance.

  Keyword arguments:
  - image: an image;
  - matches: matches;
 
  Step arguments (key, default):
  - dist: max distance, 0.5.

  Returns:
  - matches: good matches (< distance).
  

## Module: mrph
Morphological operations.
It is a set of non-linear operations that process 
images based on shapes morphology of features in an image. 
It applies structuring element to an input image and generate an output image.

### Function: erode
  Erodes away the boundaries of the foreground object and removes small-scale details 
  from an image but simultaneously reduces the size of regions of interest.
  This operation is opposite to dilation

  Keyword arguments:
  - image: an image;

  Step arguments (key, default):
  - iter: number of iterations, 3;

  Returns:
  - image: result image;
  

### Function: dilate
  Probings and expands the shapes contained in the input image. 
  This operation is opposite to erosion
  
  Keyword arguments:
  - image: an image;

  Step arguments (key, default):
  - iter: number of iterations, 3;

  Returns:
  - image: result image;
  

### Function: mex
  Performs one of following morphological operations:
  - opening: erosion followed by dilation;
  - closing: dilation followed by erosion;
  - gradient: the difference between dilation and erosion of an image.
  - top hat: the difference between input image and opening of the image.
  - black hat: the difference between the closing of the input image and input image.

  Keyword arguments:
  - image: an image;

  Step arguments (key, default):
  - shape: shape of structuring element, 0:
    - cv2.MORPH_RECT: 0;
    - cv2.MORPH_CROSS: 1;
    - cv2.MORPH_ELLIPSE: 2.
  - type: type of operations, 2:
    - cv2.MORPH_OPEN: 2;
    - cv2.MORPH_CLOSE: 3;
    - cv2.MORPH_GRADIENT: 4;
    - cv2.MORPH_TOPHAT: 5;
    - cv2.MORPH_BLACKHAT: 6; 
  - k: kernel size (3, 3), (5, 5), (7, 7), 3.

  Returns:
  - image: result image;
  

## Module: smth
Smoothing operation

### Function: bilateral
  Applies bilateral filtering to the input image

  Keyword arguments:
  - image: an image;

  Step arguments (key, default):
  - d: diameter of each pixel neighborhood that is used during filtering, 11;
  - c: filter sigma in the color space, 21;
  - s: filter sigma in the coordinate space, 7.

  Values (d, c, s):
  - (11, 21, 7)
  - (11, 41, 21)
  - (11, 61, 39)

  Returns:
  - image: result image;
  

## Module: testerNone
### Function: parseArgsNone

### Function: readConfigNone

### Function: setModulesPathNone

### Function: mainNone

### Function: uiNone

## Module: thrsh
Threshold operations

### Function: simple
  Applies a fixed-level (or optimal) threshold to each array element.

  Keyword arguments:
  - image: an image;

  Step arguments (key, default):
  - type: thresholding type, 0:
    - cv2.THRESH_BINARY: 0;
    - cv2.THRESH_BINARY_INV: 1;
    - cv2.THRESH_TRUNC: 2;
    - cv2.THRESH_TOZERO: 3;
    - cv2.THRESH_TOZERO_INV: 4;
  - thrsh: threshold value, 127;
  - otsu:  flag to use Otsu algorithm to choose the optimal threshold value, False

  Returns:
  - image: result binary image;
  

### Function: adaptive
  Applies a fixed-level (or optimal) threshold to each array element.

  Keyword arguments:
  - image: an image;

  Step arguments (key, default):
  - type: thresholding type, 0:
    - cv2.THRESH_BINARY: 0;
    - cv2.THRESH_BINARY_INV: 1;
    - cv2.THRESH_TRUNC: 2;
    - cv2.THRESH_TOZERO: 3;
    - cv2.THRESH_TOZERO_INV: 4;
  - mth: adaptive thresholding algorithm to use, 0:
    - cv2.ADAPTIVE_THRESH_MEAN_C: 0;
    - cv2.ADAPTIVE_THRESH_GAUSSIAN_C: 1.
  - na: neighborhood area, 15;
  - c: a constant which is subtracted from the mean or weighted mean calculated, 5.

  Returns:
  - image: result binary image;
  

