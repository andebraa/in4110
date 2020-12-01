from setuptools import setup
from Cython.Build import cythonize
import numpy
"""
setupfile for cython_color2gray.
to compile use
>>> python3 setup.py build_ext --inplace
Then open a ipython or simply import it into another script and run it
"""

setup(
    ext_modules = cythonize('cython_color2gray.pyx'),
    include_dirs=[numpy.get_include()]
)
