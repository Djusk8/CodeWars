# ------------  KATA DESCRIPTION ------------
"""
7 kyu - Descending Order

Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
Examples:

Input: 21445 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321

"""

# ---------------  SOLUTION ---------------
import codewars_test as test

Descending_Order = lambda num: int("".join(sorted(str(num), reverse=True)))


# ---------------  TEST CASES ---------------
test.assert_equals(Descending_Order(0), 0)
test.assert_equals(Descending_Order(15), 51)
test.assert_equals(Descending_Order(123456789), 987654321)