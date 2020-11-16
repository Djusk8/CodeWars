# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/571d42206414b103dc0006a1

8 kyu - Filling an array (part 1)

We want an array, but not just any old array, an array with contents!
Write a function that produces an array with the numbers 0 to N-1 in it.
For example, the following code will result in an array containing the numbers 0 to 4:

arr(5) // => [0,1,2,3,4]
"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def arr(n=0):
    return list(range(n))


# ---------------  TEST CASES ---------------
@test.it("Basic Tests")
def basic_tests():
    test.assert_equals(arr(4), [0,1,2,3])
    test.assert_equals(arr(0), [])
    test.assert_equals(arr(), [])
