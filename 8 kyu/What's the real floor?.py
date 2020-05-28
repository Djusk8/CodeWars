# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/574b3b1599d8f897470018f6

8 kyu - What's the real floor?

Europeans are odd people: in their buildings, the first floor is actually the ground floor and there is no 13th floor
(due to superstition).
Write a function that given an universal level (passed as an int) returns the European floor.
With the 1st floor being replaced by the ground floor and the 13th floor being removed, the numbers move down to take
their place. In case of above 13, they move down by two because there are two omitted numbers below them.
Basements (negatives) stay the same as the universal level.
More information here
Usage Examples
get_real_floor(1) == 0
get_real_floor(0) == 0
get_real_floor(5) == 4
get_real_floor(15) == 13
get_real_floor(-3) == -3
"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def get_real_floor(n):
    if n <= 0:
        return n
    elif n < 13:
        return n-1
    else:
        return n-2


# ---------------  TEST CASES ---------------
test.assert_equals(get_real_floor(1), 0)
test.assert_equals(get_real_floor(5), 4)
test.assert_equals(get_real_floor(15), 13)
