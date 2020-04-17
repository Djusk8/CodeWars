# ------------  KATA DESCRIPTION ------------
"""
8 kyu -  Convert number to reversed array of digits

Convert number to reversed array of digits

Given a random number:

    C#: long;
    C++: unsigned long;

You have to return the digits of this number within an array in reverse order.
Example:

348597 => [7,9,5,8,4,3]
"""

# ---------------  SOLUTION ---------------
import codewars_test as Test


def digitize(n):
    return [int(i) for i in reversed(str(n))]


# ---------------  TEST CASES ---------------
Test.assert_equals(digitize(35231),[1,3,2,5,3])
Test.assert_equals(digitize(23582357),[7,5,3,2,8,5,3,2])
Test.assert_equals(digitize(984764738),[8,3,7,4,6,7,4,8,9])
Test.assert_equals(digitize(45762893920),[0,2,9,3,9,8,2,6,7,5,4])
Test.assert_equals(digitize(548702838394),[4,9,3,8,3,8,2,0,7,8,4,5])

Test.describe('Random tests')
from random import randint
for x in range(37):
    y = randint(10, 99 * 2 ** x)
    Test.it('Testing %s' % y)
    Test.assert_equals(digitize(y), list(map(int, list(str(y)[::-1]))))
