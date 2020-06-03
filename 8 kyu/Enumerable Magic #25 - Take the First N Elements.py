# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/545afd0761aa4c3055001386

8 kyu - Enumerable Magic #25 - Take the First N Elements

Create a method take that accepts a list/array and a number n, and returns a list/array array of the first n elements
from the list/array.
If you need help, here's a reference:
https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range

"""


# ---------------  SOLUTION ---------------
import codewars_test as test

take = lambda a, n: a[:n]



# ---------------  TEST CASES ---------------
test.describe("Sample Tests")
print("should work for sample tests")
test.assert_equals(take([0, 1, 2, 3, 5, 8, 13], 3), [0, 1, 2], "should return the first 3 items")
