import pytest
import numpy as np
from Array import Array
"""
This module looks to test the implementation of array.py
"""

def test_call():
    instance = Array(4, 0,1,2,3)
    msg = "unit test error in call function"
    assert str(instance) == "(0, 1, 2, 3)", msg

def test_add():
    inst_add = Array(2, 0,1)
    msg = "unit test error in add function"
    assert (inst_add + 1) == [1,2], msg
    inst2 = Array(2, 1,2)
    assert (inst_add + inst2) == [1, 3], msg

def test_subtract():
    inst_sub = Array(3, 2,2,2)
    msg = "unit test error in subtract function"
    assert (inst_sub - 2) == [0, 0, 0], msg
    inst_sub2 = Array(3, 1,1,1)
    assert(inst_sub - inst_sub2) == [1,1,1], msg

def test_multiply():
    inst_mul = Array(5, 1,2,3,4,5)
    msg = "unit test error in multiply function"
    assert (inst_mul*10) == [10,20,30,40,50], msg
    inst_mul2 = Array(1, 0)
    assert(inst_mul * inst_mul2) == [0,0,0,0,0], msg

def test_get():
    inst_get = Array(2, 1,2)
    msg = "unit test error in get function"
    assert inst_get[1] == 2, msg

def test_compare():
    """
    test of == functionality. returns a single boolean if ALL elements are
    exactly the same.
    should handle two instances and an instance compared to an input array
    """
    msg = "unit test error in compare funciton"
    inst_comp = Array(2, 6,9)
    inst_comp2 = Array(2, 6,9)
    assert (inst_comp==inst_comp2), msg
    assert (inst_comp2 == (9,6)) == False, msg

def test_is_equal():
    """
    function should handle both two instances and an input function
    """
    msg = "unit test error in is_equal function"
    inst_equal = Array(3, 2,3,4)
    inst_equal2 = Array(3, 2,3,4)
    assert (inst_equal.is_equal(inst_equal2) == [1,1,1]), msg
    assert (inst_equal.is_equal((1,2,3)) == [0,0,0]), msg

def test_mean():
    msg = "unit test error in mean function"
    inst_mean = Array(4, 1,2,3,4)
    inst_mean2 = Array(6, 3,3,3,4,4,4) #protip; choose values that have a simple analytical solution
    assert (inst_mean.mean() == 2.5), msg
    assert (inst_mean2.mean() == 3.5), msg


def test_variance():
    """
    tests the mathemtaical variance. A tollerance is used due to the method
    being susceptible to roundoff errors etc 
    """
    msg = "unit test error in variance function"
    inst_var = Array(6, 3,3,3,4,4,4)
    inst_var2 = Array(4, 6,9,6,9)
    tolerance = 1E-5
    assert (inst_var.variance() - 0.25) > tolerance, msg
    assert (inst_var2.variance() - 2.25) > tolerance, msg

def test_min_element():
    msg = "unit test error in min_element function" #got creative with this one
    inst_min = Array(4, 1, 100,110, 111)
    inst_min2 = Array(2, 1,1)
    assert (inst_min.min_element() == 1), msg
    assert (inst_min2.min_element() == 1), msg

if __name__ == '__main__':
    shape = (4)
    my_array = Array(shape, 2, 3, 1, 0)
    print(my_array)
