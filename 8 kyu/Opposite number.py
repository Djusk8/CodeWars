# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/56dec885c54a926dcd001095

8 kyu - Opposite number

Very simple, given a number, find its opposite.
Examples:
1: -1
14: -14
-34: 34"""


# ---------------  SOLUTION ---------------
import codewars_test as test

opposite = lambda x: -x


# ---------------  TEST CASES ---------------
test.assert_equals(opposite(1),-1)
