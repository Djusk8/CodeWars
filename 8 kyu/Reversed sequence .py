# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/5a00e05cc374cb34d100000d

8 kyu - Reversed sequence 

Get the number n (n>0) to return the reversed sequence from n to 1.
Example : n=5 >> [5,4,3,2,1]

"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def reverse_seq(n):
    return list(range(n, 0, -1))


# ---------------  TEST CASES ---------------
test.assert_equals(reverse_seq(5),[5,4,3,2,1])
