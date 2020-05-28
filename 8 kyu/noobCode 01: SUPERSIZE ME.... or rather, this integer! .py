# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/5709bdd2f088096786000008

8 kyu - noobCode 01: SUPERSIZE ME.... or rather, this integer! 

Write a function that rearranges an integer into its largest possible value.
super_size(123456) # 654321
super_size(105)    # 510
super_size(12)     # 21
If the argument passed through is single digit or is already the maximum possible integer, your function should simply
return it.

"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def super_size(n):
    return int(''.join(sorted(str(n), reverse=True)))


# ---------------  TEST CASES ---------------
test.describe("Basic tests")
test.assert_equals(super_size(69),96)
test.assert_equals(super_size(513),531)
test.assert_equals(super_size(2017),7210)
test.assert_equals(super_size(414),441)
test.assert_equals(super_size(608719),987610)
test.assert_equals(super_size(123456789),987654321)
test.assert_equals(super_size(700000000001),710000000000)
test.assert_equals(super_size(666666),666666)
test.assert_equals(super_size(2),2)
test.assert_equals(super_size(0),0)
