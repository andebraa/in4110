import numpy as np
import cv2
import time as t

def numpy_color2gray(filename):
    """
    returns the grayscale version of given image.
    args:
        filename (string): filename of picture (must be in working directory)
    returns:
        gray (np.array): two dimentional array with grayscale values
    """
    img = cv2.imread(filename)
    global height, width
    height, width = img.shape[:2]

    weights = np.array((0.07, 0.72, 0.21)) #BGR
    gray = np.zeros((height, width), np.uint8) #i,j
    gray = img[:,:,0]*weights[0] + img[:,:,1]*weights[1] + img[:,:,2]*weights[2]
    gray=gray.astype('uint8')
    return gray


gray = numpy_color2gray('rain.jpg')

cv2.imshow('image', gray)
cv2.waitKey()
cv2.destroyAllWindows()

#extracting times from pure python method
r_file = open("python_report_color2gray.txt", 'r')
r_file.readline()
r_file.readline()
python_time = r_file.readline().split()[-1]
r_file.close()

file = open("numpy_report_color2gray.txt", 'w')

times = []
runs = 3
for i in range(runs):
    str_time = t.time()
    numpy_color2gray('rain.jpg')
    end_time = t.time()
    times.append(end_time - str_time)

file.write(f"timing: numpy_color2gray \n")
file.write(f"image dimensions: height: {height}, width: {width} \n")
file.write(f"average run after {runs} time(s): {sum(times)/runs} \n")
file.write(f"This is {float(python_time) - (sum(times)/runs)} seconds faster than python method \n")
file.write(f"timed using time")
file.close()
