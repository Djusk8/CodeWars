# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/53670c5867e9f2222f000225

7 kyu - Orthogonal Vectors

Suppose I have two vectors: (a1, a2, a3, ..., aN) and (b1, b2, b3, ..., bN). The dot product between these two vectors
is defined as:

a1*b1 + a2*b2 + a3*b3 + ... + aN*bN

The vectors are classified as orthogonal if the dot product equals zero.
Complete the function that accepts two sequences as inputs and returns true if the vectors are orthogonal, and false if
they are not. The sequences will always be correctly formatted and of the same length, so there is no need to check them
first.
Examples

[1, 1, 1], [2, 5, 7]        --> false
[1, 0, 0, 1], [0, 1, 1, 0]  --> true
"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def is_orthogonal(u, v): 
    return not sum(x*y for x,y in zip(u,v))


# ---------------  TEST CASES ---------------
@test.describe('Example Tests')
def example_tests():
    test.assert_equals(is_orthogonal([1,2], [2,1]), False)
    test.assert_equals(is_orthogonal([1,-2], [2,1]), True)
    test.assert_equals(is_orthogonal([7,8], [7,-6]), False)
    test.assert_equals(is_orthogonal([-13,-26], [-8,4]), True)
    test.assert_equals(is_orthogonal([1,2,3], [0,-3,2]), True)
    test.assert_equals(is_orthogonal([3,4,5], [6,7,-8]), False)
    test.assert_equals(is_orthogonal([3,-4,-5], [-4,-3,0]), True)
    test.assert_equals(is_orthogonal([1,-2,3,-4], [-4,3,2,-1]), True)
    test.assert_equals(is_orthogonal([2,4,5,6,7], [-14,-12,0,8,4]), True)
    test.assert_equals(is_orthogonal([5,10,1,20,2], [-2,-20,-1,10,5]), False)
