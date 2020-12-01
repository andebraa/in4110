import numpy as np
import cv2
import time as t


def python_color2sepia( picture_name):
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
    return sep


if __name__=='__main__':
    file = open("python_report_color2sepia.txt", 'w')

    times = []
    runs = 3
    for i in range(runs):
        str_time = t.time()
        sepia = python_color2sepia('rain.jpg')
        end_time = t.time()
        times.append(end_time - str_time)


    sepia = python_color2sepia('rain.jpg')
    cv2.imshow('image', sepia)
    cv2.waitKey()
    cv2.destroyAllWindows()

    file.write(f"timing: python_color2sepia \n")
    file.write(f"image dimensions: height: {height}, width: {width} \n")
    file.write(f"average run after {runs} time(s): {sum(times)/runs} \n")
    file.write(f"timed using time")
    file.close()
