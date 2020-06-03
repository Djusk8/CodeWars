# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/57eaeb9578748ff92a000009

8 kyu - Sum Mixed Array

Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
Return your answer as a number.

"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def sum_mix(arr):
    return sum(int(i) for i in arr)


# ---------------  TEST CASES ---------------
test.describe("Basic tests")
test.assert_equals(sum_mix([9, 3, '7', '3']), 22)
test.assert_equals(sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7]), 42)
test.assert_equals(sum_mix(['3', 6, 6, 0, '5', 8, 5, '6', 2,'0']), 41)
test.assert_equals(sum_mix(['1', '5', '8', 8, 9, 9, 2, '3']), 45)
test.assert_equals(sum_mix([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]), 61)
