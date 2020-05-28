# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/570a6a46455d08ff8d001002

8 kyu - No zeros for heros

Numbers ending with zeros are boring.
They might be fun in your world, but not here.
Get rid of them. Only the ending ones.
1450 -> 145
960000 -> 96
1050 -> 105
-1050 -> -105

Zero alone is fine, don't worry about it. Poor guy anyway
"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def no_boring_zeros(n):
    while n and not n % 10:
        n /= 10
    return int(n)


# ---------------  TEST CASES ---------------
def testing(actual, expected):
    test.assert_equals(actual, expected)


test.describe("common_left_edge")
test.it("Basic tests")
testing(no_boring_zeros(0), 0)
testing(no_boring_zeros(1450), 145)
testing(no_boring_zeros(960000), 96)
testing(no_boring_zeros(1050), 105)
testing(no_boring_zeros(-1050), -105)

