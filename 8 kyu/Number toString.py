# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/53934feec44762736c00044b

8 kyu - Number toString

The code gives an error!
a = 123.toString()
Fix it!
"""


# ---------------  SOLUTION ---------------
import codewars_test as test


a = str(123)

# ---------------  TEST CASES ---------------
test.assert_equals(a, '123', 'Wrong!')
