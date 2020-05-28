# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/55ed875819ae85ca8b00005c

7 kyu - Multiply array values and filter non-numeric

Your task is to write a function, which takes two arguments and returns a sequence. First argument is a sequence of
values, second is multiplier. The function should filter all non-numeric values and multiply the rest by given
multiplier.

"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def multiply_and_filter(seq, multiplier): 
    return [x * multiplier for x in seq if type(x) in (int, float)]


# ---------------  TEST CASES ---------------
@test.describe('Example Tests')
def example_tests():
    test.assert_equals(multiply_and_filter([1,2,3,4], 1.5), [1.5, 3, 4.5, 6])
    test.assert_equals(multiply_and_filter([1,2,3], 0), [0, 0, 0])
    test.assert_equals(multiply_and_filter([0,0,0], 2), [0, 0, 0])
    test.assert_equals(multiply_and_filter([1, None, lambda x: x, 2.5, 'string', 10, None, {}, []], 3), [3,7.5,30])
    test.assert_equals(multiply_and_filter([1, None, lambda x: x, 2.5, 'string', 10, None, {}, [], True, False], 3), [3,7.5,30])

