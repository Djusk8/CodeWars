# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/551b4501ac0447318f0009cd

8 kyu - Convert a Boolean to a String

Implement a function which convert the given boolean value into its string representation.

"""


# ---------------  SOLUTION ---------------
import codewars_test as test

boolean_to_string = lambda x: str(x)

# ---------------  TEST CASES ---------------
@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(boolean_to_string(True), "True")
        test.assert_equals(boolean_to_string(False), "False")
