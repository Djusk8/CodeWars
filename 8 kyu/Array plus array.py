# ------------  KATA DESCRIPTION ------------
"""
8 kyu
Array plus array

I'm new to coding and now I want to get the sum of two arrays...actually the sum of all their elements. I'll appreciate for your help.

P.S. Each array includes only integer numbers. Output is a number too.
"""

# ---------------  SOLUTION ---------------
import codewars_test as Test


def array_plus_array(arr1, arr2):
    return sum(arr1) + sum(arr2)


# ---------------  TEST CASES ---------------
Test.it("Basic test")
Test.assert_equals(array_plus_array([1, 2, 3], [4, 5, 6]), 21)
Test.assert_equals(array_plus_array([-1, -2, -3], [-4, -5, -6]), -21)
Test.assert_equals(array_plus_array([0, 0, 0], [4, 5, 6]), 15)
Test.assert_equals(array_plus_array([100, 200, 300], [400, 500, 600]), 2100)