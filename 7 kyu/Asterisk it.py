# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/5888cba35194f7f5a800008b

7 kyu - Asterisk it

Task
You are given a function that should insert an asterisk (*) between every pair of even digits in the given input, and
return it as a string. If the input is a sequence, concat the elements first as a string.
Input
The input can be an integer, a string of digits or a sequence containing integers only.
Output
Return a string.
Examples
5312708     -->  "531270*8"
"0000"      -->  "0*0*0*0"
[1, 4, 64]  -->  "14*6*4"Have fun!

"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def asterisc_it(n):
    if type(n) == list:
        n = ''.join(str(i) for i in n)
    return str(n)[0] + ''.join(('*'+y) if not (int(x)%2 or int(y)%2) else y for x,y in list(zip(str(n), str(n)[1:])))



# ---------------  TEST CASES ---------------
@test.describe('Example Tests')
def example_tests():        
    # test.assert_equals(asterisc_it(5312708), '531270*8')
    # test.assert_equals(asterisc_it(9682135), '96*8*2135')
    # test.assert_equals(asterisc_it(2222), '2*2*2*2')
    # test.assert_equals(asterisc_it(1111), '1111')
    # test.assert_equals(asterisc_it(9999), '9999')
    # test.assert_equals(asterisc_it('0000'), '0*0*0*0')
    # test.assert_equals(asterisc_it(8), '8')
    # test.assert_equals(asterisc_it(2), '2')
    # test.assert_equals(asterisc_it(0), '0')
    test.assert_equals(asterisc_it([1, 4, 64, 68, 67, 23, 1]), '14*6*4*6*8*67231')
