# ------------  KATA DESCRIPTION ------------
"""
7 kyu
Square Every Digit

Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer

"""

# ---------------  SOLUTION ---------------
import codewars_test as Test


def square_digits(num):

    result = [str(num**2) for num in map(int, str(num))]

    return int(''.join(result))


# ---------------  TEST CASES ---------------
Test.assert_equals(square_digits(9119), 811181)