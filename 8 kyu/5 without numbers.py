# ------------  KATA DESCRIPTION ------------
"""
8 kyu - 5 without numbers !!

Write a function that always returns 5

Sounds easy right? Just bear in mind that you can't use any of the following characters: 0123456789*+-/

Good luck :)

"""


# ---------------  SOLUTION ---------------
def unusual_five():
    return ord('')


# ---------------  TEST CASES ---------------
import codewars_test as test

test.describe("Basic test")
test.it("Should return 5")
test.assert_equals(unusual_five(),5,"lol")
