# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/53ee5429ba190077850011d4

8 kyu - You Can't Code Under Pressure #1

Code as fast as you can! You need to double the integer and return it.
"""

# ---------------  SOLUTION ---------------
import codewars_test as test

double_integer = lambda i: i * i

# ---------------  TEST CASES ---------------
test.assert_equals(double_integer(2), 4)
