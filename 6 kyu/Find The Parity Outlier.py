# ------------  KATA DESCRIPTION ------------
"""
6 kyu
Find The Parity Outlier

You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.
Examples

[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)


"""

# ---------------  SOLUTION ---------------
import codewars_test as test


def find_outlier(integers):
    evens = [num % 2 for num in integers]

    if evens.count(0) == 1:  # if there is one even integer in the list
        return integers[evens.index(0)]
    else:
        return integers[evens.index(1)]


# ---------------  TEST CASES ---------------
test.assert_equals(find_outlier([2, 4, 6, 8, 10, 3]), 3)
test.assert_equals(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
test.assert_equals(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)
