# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/5d6f49d85e45290016bf4718

7 kyu - Is There an Odd Bit?

Return 1 when ANY odd bit of x equals 1; 0 otherwise.
x is unsigned.
(Assume "0 index", aka the least significant bit is considered position 0)
Assume x is 32 bits.
Example:
  any_odd(2)
    will return 1 because at least one odd bit is 1 (0010).
  any_odd(170)
    will return 1 because all of the odd bits are 1 (10101010).
  any_odd(5)
    will return 0 because none of the odd bits are 1 (0101).

"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def any_odd(x):

    z = bin(x)[2::][::-1][1::2]
    return bool(sum(int(a) for a in z))


# ---------------  TEST CASES ---------------
test.assert_equals(any_odd(5), 0)
test.assert_equals(any_odd(170), 1)
test.assert_equals(any_odd(2), 1)
