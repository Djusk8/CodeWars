# ------------  KATA DESCRIPTION ------------
"""
5 kyu
Maximum subarray sum

The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]

Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.
"""

# ---------------  SOLUTION ---------------
import codewars_test as test


def maxSequence(arr):
    max_sum = 0
    for i in range(len(arr)):
        for j in range(len(arr)-i):
            sm = sum(arr[i:len(arr)-j])
            max_sum = sm if sm > max_sum else max_sum
    return max_sum


# ---------------  TEST CASES ---------------
test.describe("Tests")
test.it('should work on an empty array')
test.assert_equals(maxSequence([]), 0)
test.it('should work on the example')
test.assert_equals(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)