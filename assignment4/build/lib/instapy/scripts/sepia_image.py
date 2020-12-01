import numpy as np
import cv2


def numpy_color2sepia(input_filename, output_filename = None):
    """
    returns the sepia version of given image.
    args:
        input_filename (string): filename of picture (must be in working directory)
        output_filename (optional, string): Location and name of where sepia image is stored 
    returns:
        sepia (np.array): two dimentional array with sepia values
    """
    img = cv2.imread(input_filename)
    global height, width
    height, width = img.shape[:2]

    weights = np.array([ [ 0.393 , 0.769 , 0.189] ,[ 0.349 , 0.686 , 0.168] ,[ 0.272 , 0.534 , 0.131]])
    sepia = np.zeros((height, width, 3), np.uint8) #i,j
    print(np.shape(sepia))
    print(np.shape(weights))
    sepia = img @ np.matrix.transpose(weights)
    sepia=np.flip(sepia, axis = 2)
    np.putmask(sepia, sepia>255, 255)
    print(np.shape(sepia))
    sepia=sepia.astype('uint8')

    if output_filename != None:
        cv2.imwrite(output_filename, sepia)

    return sepia
