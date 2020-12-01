import numpy as np
import cv2

def grayscale_image(input_filename, output_filename= None):
    """
    returns the grayscale version of given image.
    args:
        filename (string): filename of picture (must be in working directory)
    returns:
        gray (np.array): two dimentional array with grayscale values
    """
    img = cv2.imread(input_filename)
    global height, width
    height, width = img.shape[:2]

    weights = np.array((0.07, 0.72, 0.21)) #BGR
    gray = np.zeros((height, width), np.uint8) #i,j
    print(np.shape(img))
    print(np.shape(weights))
    print(np.shape(img.dot(weights)))
    gray = img[:,:,0]*weights[0] + img[:,:,1]*weights[1] + img[:,:,2]*weights[2]
    gray=gray.astype('uint8')

    if output_filename != None:
        cv2.imwrite(output_filename, gray)

    return gray
