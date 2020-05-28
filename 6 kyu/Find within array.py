# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/51f082ba7297b8f07f000001

6 kyu - Find within array

We'll create a function that takes in two parameters:

a sequence (length and types of items are irrelevant)
a function (value, index) that will be called on members of the sequence and their index. The function will return
either true or false.

Your function will iterate through the members of the sequence in order until the provided function returns true; at
which point your function will return that item's index.
If the function given returns false for all members of the sequence, your function should return -1.

true_if_even = lambda value, index: value % 2 == 0
find_in_array([1,3,5,6,7], true_if_even) # --> 3
"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def find_in_array(seq, predicate): 
    for i, item in enumerate(seq):
        if predicate(item, i):
            return i
    return -1


# ---------------  TEST CASES ---------------
@test.describe('Example Tests')
def example_tests():

    true_if_even = lambda v, i: v % 2 == 0
    never_true = lambda v, i: False
    true_if_value_equals_index = lambda v, i: v == i
    true_if_length_equals_index = lambda v, i: len(v) == i
    
    test.assert_equals(find_in_array([], true_if_even) , -1)
    test.assert_equals(find_in_array([1,3,5,6,7], true_if_even) , 3)
    test.assert_equals(find_in_array([2,4,6,8], true_if_even) , 0)
    test.assert_equals(find_in_array([2,4,6,8], never_true) , -1)
    test.assert_equals(find_in_array([13,5,3,1,4,5], true_if_value_equals_index) , 4)
    test.assert_equals(find_in_array(["one","two","three","four","five","six"], true_if_length_equals_index) , 4)
    test.assert_equals(find_in_array(["bc","af","d","e"], true_if_length_equals_index) , -1)
