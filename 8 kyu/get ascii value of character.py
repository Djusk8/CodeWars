# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/55acfc59c3c23d230f00006d

8 kyu - get ascii value of character

Get ASCII value of a character.
For the ASCII table you can refer to http://www.asciitable.com/
"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def get_ascii(c):
    return ord(c)

# ---------------  TEST CASES ---------------
test.assert_equals(get_ascii("A"), 65)
test.assert_equals(get_ascii(" "), 32)
test.assert_equals(get_ascii("!"), 33)
