import numpy as np
import cv2
import time as t
from numba import njit, prange



@njit()
def sepia_image(img, output_filename = None):
    """
    returns the sepiascale version of given image.
    args:
        img (np.array): three dimentional array of indexes and BGR values of an image
    returns:
        sepia (np.array): two dimentional array with sepiascale values
    """
    height, width = img.shape[:2]
    weights = [ [ 0.393 , 0.769 , 0.189] ,[ 0.349 , 0.686 , 0.168] ,[ 0.272 , 0.534 , 0.131]]
    sep = np.zeros((height, width, 3), np.uint8) #i,j
    for i in range(height ): #only parallilze this loop.
        for j in range(width):
            for k in range(3): #bgr
                a = int(weights[k][0]*img[i][j][2] + weights[k][1]*img[i][j][1] + weights[k][2]*img[i][j][0])
                if (a < 255):
                    sep[i][j][(2-k)] = a
                else:
                    sep[i][j][(2-k)] = 255

    if output_filename != None:
        cv2.imwrite(output_filename, sep)
    return sep


if __name__=='__main__':
    img = cv2.imread('rain.jpg')
    file = open("numba_report_color2sepia.txt", 'w')
    height, width = img.shape[:2]
    times = []
    runs = 3
    for i in range(runs):
        str_time = t.time()
        sepia = sepia_image(img)
        end_time = t.time()
        times.append(end_time - str_time)


    cv2.imshow('image', sepia)
    cv2.waitKey()
    cv2.destroyAllWindows()

    #extracting times from pure python method
    r_file = open("python_report_color2sepia.txt", 'r')
    r_file.readline()
    r_file.readline()
    python_time = r_file.readline().split()[-1]
    r_file.close()

    #extracting times from numpy  method
    nump_file = open("numpy_report_color2sepia.txt", 'r')
    nump_file.readline()
    nump_file.readline()
    numpy_time = nump_file.readline().split()[-1]
    nump_file.close()

    file.write(f"timing: numba_color2sepia \n")
    file.write(f"image dimensions: height: {height}, width: {width} \n")
    file.write(f"average run after {runs} time(s): {sum(times)/runs} \n")
    file.write(f"This is {float(python_time) - (sum(times)/runs)} seconds faster than python method \n")
    file.write(f"This is also {float(numpy_time) - (sum(times)/runs)} seconds faster than numpy method \n")
    file.write(f"timed using time")
    file.close()
