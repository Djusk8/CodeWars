# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/55fab1ffda3e2e44f00000c6

8 kyu - Beginner Series #4 Cockroach

The cockroach is one of the fastest insects. Write a function which takes its speed in km per hour and returns it in cm
per second, rounded down to the integer (= floored).
For example:
cockroach_speed(1.08) == 30
Note! The input is a Real number (actual type is language dependent) and is >= 0. The result should be an Integer.
"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def cockroach_speed(s):
    return int(s * 1000 / 36)


# ---------------  TEST CASES ---------------
test.describe("Basic Tests")
test.assert_equals(cockroach_speed(1.08),30)
test.assert_equals(cockroach_speed(1.09),30)
test.assert_equals(cockroach_speed(0),0)
