# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/5174a4c0f2769dd8b1000003

7 kyu - Sort Numbers

Finish the solution so that it sorts the passed in array of numbers. If the function passes in an empty array or
null/nil value then it should return an empty array.
For example:

solution([1,2,3,10,5]) # should return [1,2,3,5,10]
solution(None) # should return []


"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def solution(nums):
    return sorted(nums) if nums else []


# ---------------  TEST CASES ---------------
test.assert_equals(solution([1,2,10,5]), [1,2,5,10])
test.assert_equals(solution(None), [])
