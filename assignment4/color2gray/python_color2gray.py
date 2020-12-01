import numpy as np
import cv2
import time as t


def python_color2gray( picture_name):
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
    return gray



file = open("python_report_color2gray.txt", 'w')

times = []
runs = 3
for i in range(runs):
    str_time = t.time()
    gray = python_color2gray('rain.jpg')
    end_time = t.time()
    times.append(end_time - str_time)

cv2.imshow('image', gray)
cv2.waitKey()
cv2.destroyAllWindows()

file.write(f"timing: python_color2gray \n")
file.write(f"image dimensions: height: {height}, width: {width} \n")
file.write(f"average run after {runs} time(s): {sum(times)/runs} \n")
file.write(f"timed using time")
file.close()
