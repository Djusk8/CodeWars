# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/541c8630095125aba6000c00

6 kyu - Sum of Digits / Digital Root

Digital root (https://en.wikipedia.org/wiki/Digital_root) is the recursive sum of all the digits in a number.
Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a
single-digit number is produced. This is only applicable to the natural numbers.

EXAMPLES

    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def digital_root(n):
    return digital_root(sum(int(i) for i in str(n))) if len(str(n)) > 1 else n


# ---------------  TEST CASES ---------------
test.assert_equals(digital_root(16), 7)
test.assert_equals(digital_root(942), 6)
test.assert_equals(digital_root(132189), 6)
test.assert_equals(digital_root(493193), 2)
