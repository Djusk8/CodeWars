# ------------  KATA DESCRIPTION ------------
"""
8 kyu - Is it even?

In this Kata we are passing a number (n) into a function. 
Your code will determine if the number passed is even (or not). 
The function needs to return either a true or false. 
Numbers may be positive or negative, integers or floats.
Floats are considered UNeven for this kata.
"""


# ---------------  SOLUTION ---------------
import codewars_test as test


is_even = lambda n:  n % 2 == 0


# ---------------  TEST CASES ---------------
@test.describe('Fixed Tests')
def fixed_tests():

    @test.it('Basic Test Cases')
    def basic_tests():
        test.assert_equals(is_even(0), True)
        test.assert_equals(is_even(0.5), False)
        test.assert_equals(is_even(1), False)
        test.assert_equals(is_even(2), True)
        test.assert_equals(is_even(-4), True)
        test.assert_equals(is_even(15), False)
        test.assert_equals(is_even(20), True)
        test.assert_equals(is_even(220), True)
        test.assert_equals(is_even(222222221), False)
        test.assert_equals(is_even(500000000), True)
