# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/55edaba99da3a9c84000003b

8 kyu - Find numbers which are divisible by given number

Complete the function which takes two arguments and returns all numbers which are divisible by the given divisor. First
argument is an array of numbers and the second is the divisor.
Example
divisible_by([1, 2, 3, 4, 5, 6], 2) == [2, 4, 6]

"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def divisible_by(numbers, divisor):
    return [x for x in numbers if not x % divisor]

# ---------------  TEST CASES ---------------
test.describe("Fixed tests")
test.assert_equals(divisible_by([1,2,3,4,5,6], 2), [2,4,6])
test.assert_equals(divisible_by([1,2,3,4,5,6], 3), [3,6])
test.assert_equals(divisible_by([0,1,2,3,4,5,6], 4), [0,4])
test.assert_equals(divisible_by([0], 4), [0])
test.assert_equals(divisible_by([1,3,5], 2), [])
