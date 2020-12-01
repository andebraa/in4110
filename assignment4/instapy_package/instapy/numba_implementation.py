import numpy as np
from numba import njit, prange

sepia_matrix = np.array([[0.131, 0.534, 0.272],
                         [0.168, 0.686, 0.349],
                         [0.189, 0.769, 0.393]])


@njit
def sepia_image(img):
    """
    returns the sepiascale version of given image.
    args:
        img (np.array): three dimentional array of indexes and BGR values of an image
    returns:
        sep (np.array): two dimentional array with sepiascale values
    """
    height, width = img.shape[:2]
    weights = [[0.131 , 0.534 , 0.272], [0.168 , 0.686 , 0.349], [0.189 , 0.769 , 0.393]]
    sep = np.zeros((height, width, 3))
    highest = 0
    for i in range(height ):
        for j in range(width):
            for k in range(3):
                a = int(weights[k][0]*img[i][j][0] +
                        weights[k][1]*img[i][j][1] +
                        weights[k][2]*img[i][j][2])
                sep[i][j][k] = a
                if a > highest:
                    highest = a
    for i in range(height):
        for j in range(width):
            for k in range(3):
                sep[i][j][k] = round(255/highest*sep[i][j][k])
    return sep



@njit
def grayscale_image(img):
    """
    returns the grayscale version of given image.
    args:
        img (np.array): three dimentional array of indexes and BGR values of an image
    returns:
        gray (np.array): two dimentional array with grayscale values
    """
    height, width = img.shape[:2]
    gray = np.zeros((height, width), np.uint8)
    for i in range(height ):
        for j in range(width ):
            gray[i][j] = round(0.07*img[i][j][0] + 0.72*img[i][j][1] + 0.21*img[i][j][2])
    return gray
