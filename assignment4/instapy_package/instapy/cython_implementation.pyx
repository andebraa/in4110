import numpy as np
cimport numpy as np
import cython
cimport cython

cpdef np.ndarray[np.uint8_t, ndim=3] sepia_image(np.ndarray[np.uint8_t, ndim=3] img):
    """
    returns the sepia version of given image.
    args:
        img (np.array): three dimentional array of indexes and BGR values of an image
    returns:
        sep (np.array): three dimentional array with sepia values
    """
    cdef int height, width
    height, width = img.shape[:2]
    cdef int i, j, k
    cdef float weights[3][3]
    weights[0][:] = [0.131 , 0.534 , 0.272]
    weights[1][:] = [0.168 , 0.686 , 0.349]
    weights[2][:] = [0.189 , 0.769 , 0.393]
    cdef float b, g, r
    cdef np.ndarray[np.float_t] bgr = np.zeros((3))
    cdef np.ndarray[np.float_t, ndim=3] sep
    sep = np.zeros((height, width, 3))
    cdef int bb, gg, rr
    for i in range(height):
        for j in range(width):
            bb = img[i][j][0]
            gg = img[i][j][1]
            rr = img[i][j][2]
            b = float(weights[0][0])*bb + \
                float(weights[0][1])*gg + \
                float(weights[0][2])*rr
            g = float(weights[1][0])*bb + \
                float(weights[1][1])*gg+ \
                float(weights[1][2])*rr
            r = float(weights[2][0])*bb + \
                float(weights[2][1])*gg + \
                float(weights[2][2])*rr
            bgr[0] = b
            bgr[1] = g
            bgr[2] = r
            sep[i][j] = bgr
    sep *= 255.0/float(sep.max())
    sep = sep.round()
    return sep


cpdef np.ndarray[np.uint8_t, ndim=2] grayscale_image(np.ndarray[np.uint8_t, ndim=3] img):
    """
    returns the grayscale version of given image.
    args:
        img (np.array): three dimentional array of indexes and BGR values of an image
    returns:
        gray (np.array): two dimentional array with grayscale values
    """
    cdef int height, width
    height, width = img.shape[:2]
    cdef int i, j

    cdef np.ndarray[np.double_t, ndim = 2] gray
    gray = np.zeros((height, width), np.float)
    for i in range(height):
        for j in range(width):
            gray[i][j] = 0.07*float(img[i][j][0]) + \
                         0.72*float(img[i][j][1]) + \
                         0.21*float(img[i][j][2])
    return gray.round()
