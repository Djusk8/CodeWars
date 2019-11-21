# ------------  KATA DESCRIPTION ------------
"""
8 kyu - Reversed Strings

Complete the solution so that it reverses the string value passed into it.

solution('world') # returns 'dlrow'
"""


# ---------------  SOLUTION ---------------
def solution(string):
    return string[::-1]


# ---------------  TEST CASES ---------------
import codewars_test as Test

Test.expect(solution('world') == 'dlrow')
Test.expect(solution('hello') == 'olleh')
Test.expect(solution('') == '')
Test.expect(solution('h') == 'h')
