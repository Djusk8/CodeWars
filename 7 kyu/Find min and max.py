# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/57a1ae8c7cb1f31e4e000130

7 kyu - Find min and max

Implement a function that returns the minimal and the maximal value of a list (in this order).

"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def get_min_max(seq): 
    return min(seq), max(seq)


# ---------------  TEST CASES ---------------
@test.describe('Example Tests')
def example_tests():
    test.assert_equals(get_min_max([1]), (1,1));
    test.assert_equals(get_min_max([1,2]), (1,2));
    test.assert_equals(get_min_max([2,1]), (1,2));
