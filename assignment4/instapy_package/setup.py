import numpy as np
from setuptools import setup, find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize


#funtion for easily printing out readme. taken from pythonhosted.org
with open("README.md", 'r') as fh:
    long_description = fh.read()

setup(
    name = 'instapy',
    version='0.1.0',
    author='Anders Bråte',
    description=(
        "Package for applying sepia og grayscale filters on images using numpy and cv2"
    ),
    #packages = ['instapy', 'tests'], #må være i denne rekkefølgen

    packages = find_packages(),
    scripts = ["bin/instapy"],
    ext_modules=cythonize(
        Extension(
        #extensions is what python calls somethig that's compiled
            "cython_implementation",
            sources = ["instapy/cython_implementation.pyx"], #setuptools supports cython, and builds it
            include_dirs=[np.get_include()], #this is to inlcude cinclude numpy in the file
        )),
    long_description=long_description,
    long_description_content_type = 'text/markdown',
    setup_requires=['numpy', 'setuptools>=18.0','cython'],
    install_requires=['opencv-python', 'numba', 'numpy']

)
