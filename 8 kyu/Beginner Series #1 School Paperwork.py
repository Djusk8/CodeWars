# ------------  KATA DESCRIPTION ------------
"""
8 kyu
Beginner Series #1 School Paperwork

Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.

Your task is to calculate how many blank pages do you need.
Example:

paperwork(5, 5) == 25

Note: if n < 0 or m < 0 return 0!

Waiting for translations and Feedback! Thanks!

"""

# ---------------  SOLUTION ---------------
import codewars_test as test


def paperwork(n, m):
    return 0 if n < 0 or m < 0 else n*m


# ---------------  TEST CASES ---------------
test.assert_equals(paperwork(5,5), 25, "Failed at Paperwork(5,5)")