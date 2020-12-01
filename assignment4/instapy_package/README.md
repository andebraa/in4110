Fork from andebraa

**improvements**
* bin/instapy
  * improved readability
  * improved argparser
  * added checks for userinput
  * implemented grayscale_image() and sepia_image()
* tests/test_instapy.py
  * improved readability
  * implemented missing tests
* setup.py
  * fixed cython build
* instapy/*
  * improved readability
  * moved cv2 imread and imwrite to instapy script
  * fixed sepia filter on all implementations
  * added normalization to sepia filter
  * improved numba and cython grayscale and sepia implementations
  * slowed down the python sepia implementation due to normalization
* requirements.txt
  * added requirements


**installation**
```bash
$ pip install -r requirements
$ pip install .
```

**usage**
```bash
$ instapy -h
$ instapy -f path/to/image.jpg -se -o output.jpg
```

**testing**
```bash
python -m pytest
```