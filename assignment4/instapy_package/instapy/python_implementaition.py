import numpy as np
import cv2

def python_color2gray( picture_name, output_filename = None ):
    """
    returns the grayscale version of given image.
    args:
        filename (string): filename of picture (must be in working directory)
    returns:
        gray (np.array): two dimentional array with grayscale values
    """
    img = cv2.imread(picture_name)
    global height, width
    height, width = img.shape[:2]

    weights = [0.07, 0.72, 0.21] #BGR
    gray = np.zeros((height, width), np.uint8) #i,j
    for i in range(height ):
        for j in range(width ):
            gray[i][j] = (0.07*img[i][j][0] + 0.72*img[i][j][1] + 0.21*img[i][j][2])
            #print(gray[i][j])
            
    
    if output_filename != None:
        cv2.imwrite(output_filename, sepia)

    return gray


def python_color2sepia( picture_name, output_filename = None):
    """
    returns the sepia version of given image.
    args:
        filename (string): filename of picture (must be in working directory)
    returns:
        sepia (np.array): two dimentional array with sepia values
    """
    img = cv2.imread(picture_name)
    global height, width
    height, width = img.shape[:2]

    #RGB!
    weights = [ [ 0.393 , 0.769 , 0.189] ,[ 0.349 , 0.686 , 0.168] ,[ 0.272 , 0.534 , 0.131]]
    sep = np.zeros((height, width, 3), np.uint8) #i,j
    for i in range(height):
        for j in range(width):
            for k in range(3): #bgr
                a = int(weights[k][0]*img[i,j,2] + weights[k][1]*img[i,j,1] + weights[k][2]*img[i,j,0])
                if (a < 255):
                    sep[i,j,(2-k)] = a
                else:
                    sep[i,j,(2-k)] = 255
                    
    if output_filename != None:
        cv2.imwrite(output_filename, sepia)           
    return sep
