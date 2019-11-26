# ------------  KATA DESCRIPTION ------------
"""
6 kyu - Bit Counting

Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

"""

# ---------------  SOLUTION ---------------
import codewars_test as test


def countBits(n):
    return bin(n).count("1")


# ---------------  TEST CASES ---------------
test.assert_equals(countBits(0), 0);
test.assert_equals(countBits(4), 1);
test.assert_equals(countBits(7), 3);
test.assert_equals(countBits(9), 2);
test.assert_equals(countBits(10), 2);