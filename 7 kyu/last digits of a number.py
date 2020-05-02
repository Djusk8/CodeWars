# ------------  KATA DESCRIPTION ------------
"""
7 kyu - last digits of a number

Your job is to write function last_digits(n,d) which return the last d digits of an integer n as a list.
n will be from 0 to 10^10
Examples:
last_digits(1,1)     --> [1]
last_digits(1234,2)   --> [3,4]
last_digits(637547,6) --> [6,3,7,5,4,7]
Special cases:
If d > the number of digits, just return the number's digits as a list.
If d <= 0, then return an empty list.
This is the first kata I have made, so please report any issues.
"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def solution(n, d):
    return [int(i) for i in str(n)[-d:]] if d > 0 else []

# ---------------  TEST CASES ---------------

test.describe('Example tests')
test.assert_equals(solution(1,1),[1])
test.assert_equals(solution(123767,4),[3,7,6,7])
test.assert_equals(solution(0,1),[0])
test.assert_equals(solution(34625647867585,10),[5,6,4,7,8,6,7,5,8,5])

test.describe('d <= 0')
test.assert_equals(solution(1234,0),[])
test.assert_equals(solution(24134,-4),[])

test.describe('d > number of digits in n')
test.assert_equals(solution(1343,5),[1,3,4,3])
