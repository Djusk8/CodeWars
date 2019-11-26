# ------------  KATA DESCRIPTION ------------
"""
8 kyu - Well of Ideas - Easy Version

For every good kata idea there seem to be quite a few bad ones!

In this kata you need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'. If there are one or two
good ideas, return 'Publish!', if there are more than 2 return 'I smell a series!'. If there are no good ideas, as is
often the case, return 'Fail!'.

"""

# ---------------  SOLUTION ---------------
import codewars_test as test


def well(x):
    gi = x.count("good")
    if gi > 2:
        return "I smell a series!"
    elif 1 <= gi <= 2:
        return "Publish!"
    else:
        return "Fail!"


# ---------------  TEST CASES ---------------
test.describe("Static Cases")
test.assert_equals(well(['bad', 'bad', 'bad']), 'Fail!')
test.assert_equals(well(['good', 'bad', 'bad', 'bad', 'bad']), 'Publish!')
test.assert_equals(well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']), 'I smell a series!')
