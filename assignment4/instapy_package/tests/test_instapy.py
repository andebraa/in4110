import cv2
import numpy as np
from random import randrange
from instapy.python_implementation import grayscale_image as python_grey
from instapy.numpy_implementation import grayscale_image as numpy_grey
from instapy.numba_implementation import grayscale_image as numba_grey
from cython_implementation import grayscale_image as cython_grey
from instapy.python_implementation import sepia_image as python_sepia
from instapy.numpy_implementation import sepia_image as numpy_sepia
from instapy.numba_implementation import sepia_image as numba_sepia
from cython_implementation import sepia_image as cython_sepia

def test_sepia():
    height = 100
    width = 150
    img = np.random.randint(255, size=(height, width, 3), dtype=np.uint8)
    r_c = (randrange(height), randrange(width))  # random coordinates

    # speia matrix
    s_m = np.array([[0.131, 0.534, 0.272],
                    [0.168, 0.686, 0.349],
                    [0.189, 0.769, 0.393]])


    py_img = python_sepia(img)
    np_img = numpy_sepia(img)
    nb_img = numba_sepia(img)
    cy_img = cython_sepia(img)

    # implementation produce same result
    np.testing.assert_array_equal(py_img, np_img)  # python/numpy
    assert np.allclose(nb_img, np_img, atol=3)     # numba/numpy
    assert np.allclose(cy_img, nb_img, atol=3)     # cython/numba

    r_p = img[r_c[0]][r_c[1]]  # random pixel

    # assert one pixel has the expected value
    s_p = np.array([r_p[0]*s_m[0][0]+r_p[1]*s_m[0][1]+r_p[2]*s_m[0][2],
                    r_p[0]*s_m[1][0]+r_p[1]*s_m[1][1]+r_p[2]*s_m[1][2],
                    r_p[0]*s_m[2][0]+r_p[1]*s_m[2][1]+r_p[2]*s_m[2][2]])
    x = np_img[r_c[0]][r_c[1]][0]/s_p[0]  # find normalization ratio
    s_p *= x  # apply normalization
    s_p = s_p.round()
    assert np.allclose(np_img[r_c[0]][r_c[1]], s_p, atol=3)

def test_grayscale():
    height = 100
    width = 150
    img = np.random.randint(255, size=(height, width, 3), dtype=np.uint8)
    r_c = (randrange(height), randrange(width))  # random coordinates

    py_img = python_grey(img)
    np_img = numpy_grey(img)
    nb_img = numba_grey(img)
    cy_img = cython_grey(img)

    # implementations produce same result
    np.testing.assert_array_equal(py_img, np_img)  # python/numpy
    np.testing.assert_array_equal(nb_img, np_img)  # numba/numpy
    assert np.allclose(cy_img, nb_img, atol=3)     # cython/numba

    # procsessed image is grayscale
    assert np_img.shape == (height, width)
    
    r_p = img[r_c[0]][r_c[1]]  # random pixel

    # random pixel has expected value
    assert cy_img[r_c[0]][r_c[1]] == round(r_p[0]*0.07+r_p[1]*0.72+r_p[2]*0.21)
