# ------------  KATA DESCRIPTION ------------
"""
8 kyu - Sum of positive

You get an array of numbers, return the sum of all of the positives ones.
Example [1,-4,7,12] => 1 + 7 + 12 = 20
Note: if there is nothing to sum, the sum is default to 0.
"""

# ---------------  SOLUTION ---------------
import codewars_test as test


def positive_sum(arr):
    return sum(x for x in arr if x > 0)


# ---------------  TEST CASES ---------------
test.describe("positive_sum")

test.it("works for some examples")
test.assert_equals(positive_sum([1,2,3,4,5]),15)
test.assert_equals(positive_sum([1,-2,3,4,5]),13)
test.assert_equals(positive_sum([-1,2,3,4,-5]),9)

test.it("returns 0 when array is empty")
test.assert_equals(positive_sum([]),0)

test.it("returns 0 when all elements are negative")
test.assert_equals(positive_sum([-1,-2,-3,-4,-5]),0)

