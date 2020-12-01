import numpy as np
from functools import reduce

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
        for j in range(width):
            gray[i][j] = round(0.07*img[i][j][0] + 0.72*img[i][j][1] + 0.21*img[i][j][2])
    return gray


def sepia_image(img):
    """
    returns the sepia version of given image.
    args:
        img (np.array): three dimentional array of indexes and BGR values of an image
    returns:
        sep (np.array): three dimentional array with sepia values
    """
    height, width = img.shape[:2]
    weights = [[0.131, 0.534, 0.272],
               [0.168, 0.686, 0.349],
               [0.189, 0.769, 0.393]]
    sep = np.zeros((height, width, 3), np.float)
    for i in range(height):
        for j in range(width):
            for k in range(3):
                sep[i][j][k] = weights[k][0]*img[i,j,0] + weights[k][1]*img[i,j,1] + weights[k][2]*img[i,j,2]
    highest = reduce(max, sep.flat)
    sep = np.array([[[round((lambda n: 255/highest*n)(bgr)) for bgr in x] for x in y] for y in sep])
    return sep
