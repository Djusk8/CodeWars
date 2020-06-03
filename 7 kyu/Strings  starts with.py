# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/5803a6d8db07c59fff00015f

7 kyu - Strings: starts with

Challenge:
Given two null-terminated strings in the arguments "string" and "prefix", determine if "string" starts with the "prefix"
string. Return 1 (or any other "truthy" value) if true, 0 if false.
Example:
startsWith("hello world!", "hello"); // should return 1.
startsWith("hello world!", "HELLO"); // should return 0.
startsWith("nowai", "nowaisir"); // should return 0.

Addendum:
For this problem, an empty "prefix" string should always return 1 (true) for any value of "string".
If the length of the "prefix" string is greater than the length of the "string", return 0.
The check should be case-sensitive, i.e. startsWith("hello", "HE") should return 0, whereas startsWith("hello", "he")
should return 1.
The length of the "string" as well as the "prefix" can be defined by the formula: 0 <= length < +Infinity
No characters should be ignored and/or omitted during the test, e.g. whitespace characters should not be ignored.

"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def starts_with(st, prefix): 
    return st.startswith(prefix)


# ---------------  TEST CASES ---------------
@test.describe('Example Tests')
def example_tests():

    # Basic Tests: Test the basic behavior (basic understanding of the task).
    @test.it('Basic Test Cases')
    def basic_tests():
        test.assert_equals(starts_with("hello world!", "hello"), True)
        test.assert_equals(starts_with("hello world!", "HELLO"), False)
        test.assert_equals(starts_with("nowai", "nowaisir"), False)

    # Edge Cases: Test the edge cases, which are not common but hard to correctly solve.
    # These are needed because "rare but hard cases" are not well-covered by random tests only.
    @test.it('Edge Cases')
    def edge_case_tests():
        test.assert_equals(starts_with("", ""), True)
        test.assert_equals(starts_with("abc", ""), True)
        test.assert_equals(starts_with("", "abc"), False)
