# ------------  KATA DESCRIPTION ------------
"""
8 kyu
Grasshopper - Summation

Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

For example:

summation(2) -> 3
1 + 2

summation(8) -> 36
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
"""

# ---------------  SOLUTION ---------------
import codewars_test as test


def summation(num):
    return sum([x for x in range(num+1)])


# ---------------  TEST CASES ---------------
test.describe('Summation')
test.it('Should return the correct total')
test.assert_equals(summation(1), 1)
test.assert_equals(summation(8), 36)