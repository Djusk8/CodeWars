# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/57f781872e3d8ca2a000007e

8 kyu - Beginner - Lost Without a Map

Given an array of integers, return a new array with each value doubled.
For example:
[1, 2, 3] --> [2, 4, 6]
For the beginner, try to use the map method - it comes in very handy quite a lot so is a good one to know.

"""


# ---------------  SOLUTION ---------------
import codewars_test as test

maps = lambda a: [i*2 for i in a]


# ---------------  TEST CASES ---------------
test.describe("Sample tests")
test.assert_equals(maps([1, 2, 3]), [2, 4, 6])
test.assert_equals(maps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])
test.assert_equals(maps([]), [])
