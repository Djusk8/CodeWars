# ------------  KATA DESCRIPTION ------------
"""
7 kyu - Debug Sum of Digits of a Number

Debug   function getSumOfDigits that takes positive integer to calculate sum of it's digits. Assume that argument is an integer.
Example
123  => 6
223  => 7
1337 => 15"""

# ---------------  SOLUTION ---------------
import codewars_test as test


def get_sum_of_digits(num):
    return sum(int(i) for i in str(num))


# ---------------  TEST CASES ---------------
test.assert_equals(get_sum_of_digits(123), 6)
