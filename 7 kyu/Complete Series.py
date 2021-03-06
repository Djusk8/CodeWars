# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/580a4001d6df740d61000301

7 kyu - Complete Series

You are given an array of non-negative integers, your task is to complete the series from 0 to the highest number in the
array.
If the numbers in the sequence provided are not in order you should order them, but if a value repeats, then you must
return a sequence with only one item, and the value of that item must be 0. like this:
inputs        outputs
[2,1]     ->  [0,1,2]
[1,4,4,6] ->  [0]

Notes: all numbers are positive integers.
This is set of example outputs based on the input sequence.
inputs        outputs
[0,1]   ->    [0,1]
[1,4,6] ->    [0,1,2,3,4,5,6]
[3,4,5] ->    [0,1,2,3,4,5]
[0,1,0] ->    [0]
"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def complete_series(seq): 
    return [0] if len(seq) != len(set(seq)) else [x for x in range(max(seq)+1)]


# ---------------  TEST CASES ---------------
@test.describe('Example Tests')
def example_tests():
    test.assert_equals(complete_series([0,1]), [0,1])
    test.assert_equals(complete_series([1,4,6]), [0,1,2,3,4,5,6])
    test.assert_equals(complete_series([3,4,5]), [0,1,2,3,4,5])
    test.assert_equals(complete_series([2,1]), [0,1,2])
    test.assert_equals(complete_series([1,4,4,6]), [0])
