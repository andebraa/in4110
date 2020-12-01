import numpy as np
import cv2
import time as t

def numpy_color2sepia(filename):
    """
    returns the sepia version of given image.
    args:
        filename (string): filename of picture (must be in working directory)
    returns:
        sepia (np.array): two dimentional array with sepia values
    """
    img = cv2.imread(filename)
    global height, width
    height, width = img.shape[:2]

    weights = np.array([ [ 0.393 , 0.769 , 0.189] ,[ 0.349 , 0.686 , 0.168] ,[ 0.272 , 0.534 , 0.131]])
    sepia = np.zeros((height, width, 3), np.uint8) #i,j
    sepia = img @ np.matrix.transpose(weights)
    sepia=np.flip(sepia, axis = 2)
    np.putmask(sepia, sepia>255, 255)
    sepia=sepia.astype('uint8')

    return sepia

if __name__=='__main__':
    sepia = numpy_color2sepia('rain.jpg')

    cv2.imshow('image', sepia)
    cv2.waitKey()
    cv2.destroyAllWindows()

    #extracting times from pure python method
    r_file = open("python_report_color2sepia.txt", 'r')
    r_file.readline()
    r_file.readline()
    python_time = r_file.readline().split()[-1]
    r_file.close()

    file = open("numpy_report_color2sepia.txt", 'w')

    times = []
    runs = 3
    for i in range(runs):
        str_time = t.time()
        sepia = numpy_color2sepia('rain.jpg')
        end_time = t.time()
        times.append(end_time - str_time)

    cv2.imshow('image', sepia)
    cv2.waitKey()
    cv2.destroyAllWindows()

    file.write(f"timing: numpy_color2sepia \n")
    file.write(f"image dimensions: height: {height}, width: {width} \n")
    file.write(f"average run after {runs} time(s): {sum(times)/runs} \n")
    file.write(f"This is {float(python_time) - (sum(times)/runs)} seconds faster than python method \n")
    file.write(f"timed using time")
    file.close()
