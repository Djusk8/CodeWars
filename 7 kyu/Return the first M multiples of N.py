# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/593c9175933500f33400003e

7 kyu - Return the first M multiples of N

Implement a function, multiples(m, n), which returns an array of the first m multiples of the real number n. Assume that
m is a positive integer.
Ex.
multiples(3, 5.0)
should return
[5.0, 10.0, 15.0]"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def multiples(m, n):
    return [n*(i+1) for i in range(m)]


# ---------------  TEST CASES ---------------
@test.it("Sample Tests")
def sample_tests():
    test.assert_equals(multiples(3, 5), [5, 10, 15])
