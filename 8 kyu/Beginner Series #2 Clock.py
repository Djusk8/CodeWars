# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a

8 kyu - Beginner Series #2 Clock

Clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.
Your task is to make 'Past' function which returns time converted to milliseconds.
Example:
past(0, 1, 1) == 61000
Input constraints: 0 <= h <= 23, 0 <= m <= 59, 0 <= s <= 59
"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def past(h, m, s):
    return 1000*(s+m*60+h*3600)

# ---------------  TEST CASES ---------------
test.assert_equals(past(0,1,1),61000)
test.assert_equals(past(1,1,1),3661000)
test.assert_equals(past(0,0,0),0)
test.assert_equals(past(1,0,1),3601000)
test.assert_equals(past(1,0,0),3600000)
