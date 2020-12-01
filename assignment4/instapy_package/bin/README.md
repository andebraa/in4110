Instapy package version 0.1.0

instapy.scripts:
    seipa_image(input_filename, output_filename = None):
        returns the sepia version of given image.
        args:
            input_filename (string): filename of picture (must be in working directory)
            output_filename (optional, string): Location and name of where sepia image is stored
        returns:
            sepia (np.array): two dimentional array with sepia values

    grayscale_image(input_filename, output_filename = None):
        returns the grayscale version of given image.
        args:
            filename (string): filename of picture (must be in working directory)
        returns:
            gray (np.array): two dimentional array with grayscale values
