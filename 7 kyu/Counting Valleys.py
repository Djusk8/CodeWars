# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/5da9973d06119a000e604cb6

7 kyu - Counting Valleys

You need count how many valleys you will pass.
Start is always from zero level.
Every time you go down below 0 level counts as an entry of a valley, and as you go up to 0 level from valley counts as
an exit of a valley.
One passed valley is equal one entry and one exit of a valley.
s='FUFFDDFDUDFUFUF'
U=UP
F=FORWARD
D=DOWN

To represent string above
(level 1)  __
(level 0)_/  \         _(exit we are again on level 0)
(entry-1)     \_     _/
(level-2)       \/\_/

So here we passed one valley

"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def counting_valleys(s): 
    s = s.replace('F', '')  # remove useless F's
    n = [0, ]
    for i in s:
        n.append(n[-1] + (1 if i == 'U' else -1))
    n = ','.join(map(str, n))
    return n.count("-1,0")


# ---------------  TEST CASES ---------------
@test.describe('Example Tests')
def example_tests():
    test.assert_equals(counting_valleys('DDUDDDFDUFFDUDFDFFUFDDFFDFDUFDUDFUDDDDFUDDDFFUFDUFUUDUFDFUFFFDUFUUDUDUDUUFDUDF'), 0)
    test.assert_equals(counting_valleys('DFFFD'), 0)
    test.assert_equals(counting_valleys('UFFFU'), 0)
    test.assert_equals(counting_valleys('DFFFU'), 1)
    test.assert_equals(counting_valleys('UFFDDFDUDFUFU'), 1)
    test.assert_equals(counting_valleys('UFFDDFDUDFUFUUFFDDFDUDFUFU'), 2)
    test.assert_equals(counting_valleys('UFFDDFDUDFUFUUFFDDUFFDDUFFDDUDUDUDUDUDUUUUUUUUU'), 3)
    test.assert_equals(counting_valleys('UFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFU'), 4)
    test.assert_equals(counting_valleys('UFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFU'), 6)
