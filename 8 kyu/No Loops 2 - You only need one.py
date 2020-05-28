# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/57cc40b2f8392dbf2a0003ce

8 kyu - No Loops 2 - You only need one

* No Loops Allowed *
You will be given an array (a) and a value (x). All you need to do is check whether the provided array contains the
value, without using a loop.
Array can contain numbers or strings. X can be either. Return true if the array contains the value, false if not. With
strings you will need to account for case.
Looking for more, loop-restrained fun? Check out the other kata in the series:
 https://www.codewars.com/kata/no-loops-1-small-enough
 https://www.codewars.com/kata/no-loops-3-copy-within
"""


# ---------------  SOLUTION ---------------
import codewars_test as test

check = lambda a,x: x in a


# ---------------  TEST CASES ---------------
@test.describe("Sample Test Cases")
def example_tests():
    test.assert_equals(check([66, 101], 66), True)
    test.assert_equals(check([80, 117, 115, 104, 45, 85, 112, 115], 45), True)
    test.assert_equals(check(['t', 'e', 's', 't'], 'e'), True)
    test.assert_equals(check(['what', 'a', 'great', 'kata'], 'kat'), False)
