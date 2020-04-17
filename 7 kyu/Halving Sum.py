# ------------  KATA DESCRIPTION ------------
"""
7 kyu
Halving Sum

Task

Given a positive integer n, calculate the following sum:

n + n/2 + n/4 + n/8 + ...

All elements of the sum are the results of integer division.
Example

25  =>  25 + 12 + 6 + 3 + 1 = 47
"""

# ---------------  SOLUTION ---------------
import codewars_test as test


def halving_sum(n):
    return int(n) + halving_sum(n/2) if n >= 1 else 0


# ---------------  TEST CASES ---------------
@test.describe('Example Tests')
def example_tests():
    test.assert_equals(halving_sum(25), 47)
    test.assert_equals(halving_sum(127), 247)
