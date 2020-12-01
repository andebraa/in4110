import pytest
import numpy as np
"""
This module looks to recreate the functionality of python Arrays.
"""

class Array():
    def __init__(self, shape, *args):
        self.shape = shape
        self.args = args

    def __str__(self):
        return(str(self.args))

    def __getitem__(self, key):
        return(self.args[key])

    def __add__(self, arg):
        """
        if arg is array of same size as instance add elements element wise.
        if one number is passed as arg add this to all alements of instance
        """
        res = []
        if isinstance(arg, float) or isinstance(arg, int):
            for i in range(self.shape):
                res.append(self.args[i] + arg)

        elif arg.shape == 1:
            for i in range(self.shape):
                res.append(self.args[i] + arg.args[0]) #note, arg.args[0] to handle (0,) issues in multiply

        elif self.shape != arg.shape and arg.shape != 1:
            raise ValueError(f"operands could not be brodcast together with shapes {self.shape} and {np.shape(arg)}")

        elif arg.shape == self.shape:
            for i in range(self.shape):
                res.append(self.args[i] + arg.args[i])
        return res

    def __radd__(self, arg):
        """
        Handles the special case of int + instance, where as instance + int would work
        """
        return self.__add__(arg)

    def __sub__(self, arg):
        """
        if arg is array of same size as instance subtract elements element wise.
        if one number is passed as arg subtract this from all alements of instance

        returns: list
        """
        res = []
        if isinstance(arg, float) or isinstance(arg, int):
            for i in range(self.shape):
                res.append(self.args[i] - arg)

        elif arg.shape == 1:
            for i in range(self.shape):
                res.append(self.args[i] - arg.args[0])

        elif self.shape != arg.shape and arg.shape != 1:
            raise ValueError(f"operands could not be brodcast together with shapes {self.shape} and {np.shape(arg)}")

        elif arg.shape == self.shape:
            for i in range(self.shape):
                res.append(self.args[i] - arg.args[i])
        return res

    def __rsub__(self, arg):
        return self.__sub__(arg)

    def __mul__(self, arg):
        """
        if arg is array of same size as instance subtract elements element wise.
        if one number is passed as arg subtract this from all alements of instance
        """
        res = []
        if isinstance(arg, float) or isinstance(arg, int):
            for i in range(self.shape):
                res.append(self.args[i] * arg)

        elif arg.shape == 1:
            for i in range(self.shape):
                res.append(self.args[i] * arg.args[0])

        elif self.shape != arg.shape and arg.shape != 1:
            raise ValueError(f"operands could not be brodcast together with shapes {self.shape} and {np.shape(arg)}")

        elif arg.shape == self.shape:
            for i in range(self.shape):
                res.append(self.args[i] * arg.args[i])
        return res

    def __rmul__(self, arg):
        return self.__mul__(arg)

    def __eq__(self, arg):
        """
        compares two arrays. if argument is single int or float and self
        array has single argument then these are compared
        """
        if isinstance(arg, float) or isinstance(arg, int) and self.shape ==1:
            return self.args[0] == arg #arg is float or int
        elif isinstance(arg, Array):

            #return all(self.args == arg.args)
            for i in range(arg.shape):
                if (self.args[i] != arg.args[i]): # arg is instance
                    return False
                return True
        else:
            #return all(self.args == arg)
            for i in range(self.shape):
                print(self.args[i])
                if (self.args[i] != arg[i]): # arg = (0,1,2,3)
                    return False
                return True


    def is_equal(self, arg):
        """
        compares two arrays, returns an array of equal size with boolean values
        if argument is a float or int, and instance is one number it will still compare.

        """
        res = []
        if isinstance(arg, float) or isinstance(arg, int) and self.shape ==1:
            res.append(self.args[0] == arg) #arg is float or int
            return res
        elif isinstance(arg, Array):

            #return all(self.args == arg.args)
            for i in range(arg.shape):
                res.append(self.args[i] == arg.args[i]) # arg is instance
            return res
        else:
            #return all(self.args == arg)
            for i in range(self.shape):
                print(self.args[i])
                res.append(self.args[i] == arg[i]) # arg = (0,1,2,3)
            return res

    def mean(self):
        """
        return the mathematical mean by summing over each instance argument.
        must be used with an instance
        """
        n = self.shape
        res = 0;
        for i in range(n):
            res += self.args[i]
        return (1/n)*res

    def variance(self):
        """
        calculates the mathematical variance using the mean function.
        must be used with an instance
        """
        n = self.shape
        res = 0
        mean = self.mean()
        for i in range(n):
            res += (self.args[i] - mean)**2
        return (1/(n-1))*res

    def min_element(self):
        """
        this seems unneccesary, unless i've misunderstood a whole lot
        """
        return min(self.args)


if __name__ == '__main__':
    shape = (4)
    my_array = Array(shape, 2,3,4,5)
    your_array = Array(shape, 1,2,3,4)

    print(5 * my_array)
