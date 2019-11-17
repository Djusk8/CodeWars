# ------------  KATA DESCRIPTION ------------
"""
6 kyu - Find the unique number

There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

It’s guaranteed that array contains more than 3 numbers.

The tests contain some very huge arrays, so think about performance.
"""

# ---------------  SOLUTION ---------------
import codewars_test as test


def find_uniq(arr):
    for n in set(arr):
        if arr.count(n) == 1:
            return n


# ---------------  TEST CASES ---------------
test.describe("Basic Tests")
test.assert_equals(find_uniq([ 1, 1, 1, 2, 1, 1 ]), 2)
test.assert_equals(find_uniq([ 0, 0, 0.55, 0, 0 ]), 0.55)
test.assert_equals(find_uniq([ 3, 10, 3, 3, 3 ]), 10)
