# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/59f7fc109f0e86d705000043

7 kyu - By 3, or not by 3? That is the question . . .

A trick I learned in elementary school to determine whether or not a number was divisible by three is to add all of the
integers in the number together and to divide the resulting sum by three. If there is no remainder from dividing the sum
by three, then the original number is divisible by three as well.
Given a series of numbers as a string, determine if the number represented by the string is divisible by three.
You can expect all test case arguments to be strings representing values greater than 0.
Example:
"123"      -> true
"8409"     -> true
"100853"   -> false
"33333333" -> true
"7"        -> false"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def divisible_by_three(st): 
    return not sum([int(num) for num in st]) % 3

# ---------------  TEST CASES ---------------
@test.describe('Basic Test Cases')
def basic_tests():
    test.assert_equals(divisible_by_three('123'), True, "Should return true if the sum of the given digits is divisible by 3.")
    test.assert_equals(divisible_by_three('19254'), True, "Should return true if the sum of the given digits is divisible by 3.")
    test.assert_equals(divisible_by_three('88'), False, "Should return false if the sum of the given digits is not divisible by 3.")
    test.assert_equals(divisible_by_three('1'), False, "Should return false if the sum of the given digits is not divisible by 3.")
