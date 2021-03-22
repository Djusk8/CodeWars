# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/56200d610758762fb0000002

8 kyu - Grasshopper - Basic Function Fixer


FIX THE FUNCTION
I created this function to add five to any number that was passed in to it and return the new value.
It doesn't throw any errors but it returns the wrong number.
Can you help me fix the function?

"""


# ---------------  SOLUTION ---------------
import codewars_test as test

add_five = lambda num: num + 5

# ---------------  TEST CASES ---------------

@test.describe('fix add five')
def fixed_tests():

    # Basic Tests: Test the basic behavior (basic understanding of the task).
    @test.it('Basic Test Cases')
    def basic_tests():
        test.assert_equals(add_five(5), 10)
        test.assert_equals(add_five(0), 5)
        test.assert_equals(add_five(-5), 0)
