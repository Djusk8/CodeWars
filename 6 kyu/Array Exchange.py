# ------------  KATA DESCRIPTION ------------
"""
6 kyu- Array Exchange

Array Exchange and Reversing

It's time for some array exchange! The objective is simple: exchange the elements of two arrays in-place in a way that their new content is also reversed.

# before
my_list = ['a', 'b', 'c']
other_list = [1, 2, 3]

exchange_with(my_list, other_list)

# after
my_list == [3, 2, 1]
other_list == ['c', 'b', 'a']

"""

# ---------------  SOLUTION ---------------
import codewars_test as Test


def exchange_with(a, b):

    ar = [i for i in a[::-1]]
    a.clear()

    br = [i for i in b[::-1]]
    b.clear()

    b += ar
    a += br

    pass


# ---------------  TEST CASES ---------------
a = ["1", "2", "3", "4", "5", "6", "7"]
b = ["a", "b", "c"]
exchange_with(a, b)
Test.assert_equals(a, ["c", "b", "a"])
Test.assert_equals(b, ["7", "6", "5", "4", "3", "2", "1"])