# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/5841f680c5c9b092950001ae

7 kyu - Series of integers from m to n

Task
Write a function that accepts two arguments and generates a sequence containing the integers from the first argument to
the second inclusive.
Input
Pair of integers greater than or equal to 0. The second argument will always be greater than or equal to the first.
Example
generate_integers(2, 5) # --> [2, 3, 4, 5]
"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def generate_integers(m, n): 
    return list(range(m, n+1))


# ---------------  TEST CASES ---------------
@test.describe('Example Tests')
def example_tests():
    test.assert_equals(generate_integers(2, 5), [2, 3, 4, 5])
