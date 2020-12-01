import numpy as np


def sepia_image(img):
    """
    returns the sepia version of given image.
    args:
        img (np.array): three dimentional array of indexes and BGR values of an image
    returns:
        sep (np.array): three dimentional array with sepia values
    """
    height, width = img.shape[:2]
    weights = np.array([[ 0.189 , 0.769 , 0.393] ,[ 0.168 , 0.686 , 0.349] ,[ 0.131 , 0.534 , 0.272]])
    sepia = np.zeros((height, width, 3), np.uint8)
    sepia = img @ np.matrix.transpose(weights)
    sepia=np.flip(sepia, axis = 2)
    sepia *= 255/sepia.max()
    sepia = sepia.round()
    return sepia

def grayscale_image(img):
    """
    returns the grayscale version of given image.
    args:
        img (np.array): three dimentional array of indexes and BGR values of an image
    returns:
        gray (np.array): two dimentional array with grayscale values
    """
    height, width = img.shape[:2]

    weights = np.array((0.07, 0.72, 0.21))
    gray = np.zeros((height, width), np.uint8)
    gray = img[:,:,0]*weights[0] + img[:,:,1]*weights[1] + img[:,:,2]*weights[2]
    gray = gray.round()
    return gray
