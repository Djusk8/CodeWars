# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/55f73be6e12baaa5900000d4

8 kyu - Grasshopper - Messi goals function

Messi goals function
Messi is a soccer player with goals in three leagues:

LaLiga
Copa del Rey
Champions

Complete the function to return his total number of goals in all three leagues.
Note: the input will always be valid.
For example:
5, 10, 2  -->  17"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def goals(*goals):
    return sum(goals)


# ---------------  TEST CASES ---------------
test.assert_equals(goals(0, 0, 0), 0)
test.assert_equals(goals(5, 10, 2), 17)
