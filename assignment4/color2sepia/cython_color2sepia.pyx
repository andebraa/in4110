import numpy as np
cimport numpy as np
import cv2
#import cython as c
import time as t


cdef np.ndarray[np.double_t, ndim = 2] python_color2sepia( str picture_name):
#def python_color2sepia(picture_name):
    """
    returns the sepiascale version of given image.
    args:
        filename (string): filename of picture (must be in working directory)
    returns:
        sepia (np.array): two dimentional array with sepiascale values

    """
    cdef np.ndarray[ unsigned char, ndim = 3] img
    img = cv2.imread(picture_name)

    cdef int height, width
    height, width = img.shape[:2]
    cdef int i, j, k

    weights = [ [ 0.393 , 0.769 , 0.189] ,[ 0.349 , 0.686 , 0.168] ,[ 0.272 , 0.534 , 0.131]]
    cdef np.ndarray[np.double_t, ndim = 2] sepia
    sep = np.zeros((height, width, 3), np.uint8) #i,j
    for i in range(height ):
        for j in range(width ):
          for k in range(3): #bgr
              a = int(weights[k][0]*img[i][j][2] + weights[k][1]*img[i,j,1] + weights[k][2]*img[i,j,0])
              if (a < 255):
                  sep[i][j][(2-k)] = a
              else:
                  sep[i][j][(2-k)] = 255
    return sep


if __name__=='__main__':
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

  #extracting times from numba  method
  numba_file = open("numba_report_color2sepia.txt", 'r')
  numba_file.readline()
  numba_file.readline()
  numba_time = numba_file.readline().split()[-1]
  numba_file.close()


  file = open("cython_report_color2sepia.txt", 'w')

  times = []
  runs = 3
  for i in range(runs):
      str_time = t.time()
      sepia = python_color2sepia('rain.jpg')
      end_time = t.time()
      times.append(end_time - str_time)

  #extracting picture size
  img = cv2.imread('rain.jpg')
  cdef int height, width
  height, width = img.shape[:2]

  cv2.imshow('image', sepia)
  cv2.waitKey()
  cv2.destroyAllWindows()


  file.write(f"timing: python_color2sepia \n")
  file.write(f"image dimensions: height: {height}, width: {width} \n")
  file.write(f"average run after {runs} time(s): {sum(times)/runs} \n")
  file.write(f"This is {float(python_time) - (sum(times)/runs)} seconds faster/slower than python method \n")
  file.write(f"This is {float(numpy_time) - (sum(times)/runs)} seconds faster/slower than numpy method \n")
  #file.write(f"This is {float(numba_time) - (sum(times)/runs)} seconds faster/slower than numba method \n")
  file.write(f"timed using time")
  file.close()
