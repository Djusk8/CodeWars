# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/55cbc3586671f6aa070000fb

8 kyu - Grasshopper - Check for factor

This function should test if the factor is a factor of base.
Return true if it is a factor or false if it is not.
About factors
Factors are numbers you can multiply together to get another number.
2 and 3 are factors of 6 because: 2 * 3 = 6

You can find a factor by dividing numbers. If the remainder is 0 then the number is a factor.
You can use the mod operator (%) in most languages to check for a remainder

For example 2 is not a factor of 7 because: 7 % 2 = 1
Note: base is a non-negative number, factor is a positive number.

"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def check_for_factor(base, factor):
    return not base % factor


# ---------------  TEST CASES ---------------
test.describe("Should return True")
test.assert_equals(check_for_factor(10, 2), True)
test.assert_equals(check_for_factor(63, 7), True)
test.assert_equals(check_for_factor(2450, 5), True)
test.assert_equals(check_for_factor(24612, 3), True)

test.describe("Should return False")
test.assert_equals(check_for_factor(9, 2), False)
test.assert_equals(check_for_factor(653, 7), False)
test.assert_equals(check_for_factor(2453, 5), False)
test.assert_equals(check_for_factor(24617, 3), False)
