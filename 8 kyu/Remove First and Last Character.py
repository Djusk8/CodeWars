# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0

8 kyu - Remove First and Last Character

It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string.
You're given one parameter, the original string.  You don't have to worry with strings with less than two characters.

"""


# ---------------  SOLUTION ---------------
import codewars_test as test

remove_char = lambda s: s[1: -1]


# ---------------  TEST CASES ---------------
test.describe("Tests")
test.assert_equals(remove_char('eloquent'), 'loquen')
test.assert_equals(remove_char('country'), 'ountr')
test.assert_equals(remove_char('person'), 'erso')
test.assert_equals(remove_char('place'), 'lac')
test.assert_equals(remove_char('ok'), '')
