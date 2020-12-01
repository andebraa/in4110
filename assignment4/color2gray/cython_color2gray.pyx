import numpy as np
cimport numpy as np
import cv2
import cython as c
import time as t


cdef np.ndarray[np.double_t, ndim = 2] python_color2gray( str picture_name):
#def python_color2gray(picture_name):
    """
    returns the grayscale version of given image.
    args:
        filename (string): filename of picture (must be in working directory)
    returns:
        gray (np.array): two dimentional array with grayscale values

    """
    cdef np.ndarray[ unsigned char, ndim = 3] img
    img = cv2.imread(picture_name)

    cdef int height, width
    height, width = img.shape[:2]
    cdef int i, j

    weights = [0.07, 0.72, 0.21] #BGR
    cdef np.ndarray[np.double_t, ndim = 2] gray
    gray = np.zeros((height, width), np.float) #i,j
    for i in range(height ):
        for j in range(width ):
            avg = 0
            gray[i][j] = (0.07*img[i][j][0] + 0.72*img[i][j][1] + 0.21*img[i][j][2])
            #print(gray[i][j])
    return gray



#extracting times from pure python method
r_file = open("python_report_color2gray.txt", 'r')
r_file.readline()
r_file.readline()
python_time = r_file.readline().split()[-1]
r_file.close()

#extracting times from numpy  method
nump_file = open("numpy_report_color2gray.txt", 'r')
nump_file.readline()
nump_file.readline()
numpy_time = nump_file.readline().split()[-1]
nump_file.close()

#extracting times from numba  method
numba_file = open("numba_report_color2gray.txt", 'r')
numba_file.readline()
numba_file.readline()
numba_time = numba_file.readline().split()[-1]
numba_file.close()

file = open("cython_report_color2gray.txt", 'w')

times = []
runs = 3
for i in range(runs):
    str_time = t.time()
    python_color2gray('rain.jpg')
    end_time = t.time()
    times.append(end_time - str_time)

#extracting picture size
img = cv2.imread('rain.jpg')
cdef int height, width
height, width = img.shape[:2]


file.write(f"timing: python_color2gray \n")
file.write(f"image dimensions: height: {height}, width: {width} \n")
file.write(f"average run after {runs} time(s): {sum(times)/runs} \n")
file.write(f"This is {float(python_time) - (sum(times)/runs)} seconds faster/slower than python method \n")
file.write(f"This is {float(numpy_time) - (sum(times)/runs)} seconds faster/slower than numpy method \n")
file.write(f"This is {float(numba_time) - (sum(times)/runs)} seconds faster/slower than numba method \n")
file.write(f"timed using time")
file.close()
