# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/5a262cfb8f27f217f700000b

7 kyu - Unique string characters

In this Kata, you will be given two strings a and b and your task will be to return the characters that are not common
in the two strings.
For example:
solve("xyab","xzca") = "ybzc"
--The first string has 'yb' which is not in the second string.
--The second string has 'zc' which is not in the first string.
Notice also that you return the characters from the first string concatenated with those from the second string.
More examples in the tests cases.
Good luck!
Please also try Simple remove duplicates
"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def solve(a, b):
    return ''.join(i for i in (a+b) if (i in a and i not in b) or (i not in a and i in b))


# ---------------  TEST CASES ---------------
test.it("Basic tests")
test.assert_equals(solve("xyab","xzca"),"ybzc")
test.assert_equals(solve("xyabb","xzca"),"ybbzc")
test.assert_equals(solve("abcd","xyz"),"abcdxyz")
test.assert_equals(solve("xxx","xzca"),"zca")
