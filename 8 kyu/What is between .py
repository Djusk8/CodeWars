# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/55ecd718f46fba02e5000029

8 kyu - What is between?

Complete the function that takes two integers (a, b, where a < b) and return an array of all integers between the input
parameters, including them.
For example:
a = 1
b = 4
--> [1, 2, 3, 4]
"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def between(a, b):
    return list(range(a, b+1))


# ---------------  TEST CASES ---------------
test.assert_equals(between(1, 4), [1, 2, 3, 4])
test.assert_equals(between(-2, 2), [-2, -1, 0, 1, 2])

