# ------------  KATA DESCRIPTION ------------
"""
8 kyu
Find the smallest integer in the array

Given an array of integers your solution should find the smallest integer.

For example:

    Given [34, 15, 88, 2] your solution will return 2
    Given [34, -345, -1, 100] your solution will return -345

You can assume, for the purpose of this kata, that the supplied array will not be empty.

"""

# ---------------  SOLUTION ---------------
import codewars_test as test


find_smallest_int = min


# ---------------  TEST CASES ---------------
test.assert_equals(find_smallest_int([78, 56, 232, 12, 11, 43]), 11)
test.assert_equals(find_smallest_int([78, 56, -2, 12, 8, -33]), -33)
test.assert_equals(find_smallest_int([0, 1-2**64, 2**64]), 1-2**64)