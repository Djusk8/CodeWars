# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/5966e33c4e686b508700002d

8 kyu - Sum The Strings

Create a function that takes 2 positive integers in form of a string as an input, and outputs the sum (also as a
string):

  sumStr("4", "5")    // should output "9"
  sumStr("34", "5")   // should output "39"

If either input is an empty string, consider it as zero.

"""


# ---------------  SOLUTION ---------------
import codewars_test as test

# sum_str = lambda a,b: str(int(a) + int(b))

def sum_str(a, b):
    return str(int(a) + int(b))


# ---------------  TEST CASES ---------------
test.assert_equals(sum_str("4","5"), "9")
test.assert_equals(sum_str("34","5"), "39")

