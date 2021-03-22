# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/5a63948acadebff56f000018

7 kyu - Product Of Maximums Of Array (Array Series #2) 

Introduction and Warm-up (Highly recommended)
Playing With Lists/Arrays Series

Task
Given an array/list [] of integers , Find the product of the k maximal numbers.

Notes

Array/list size is at least 3 .

Array/list's numbers Will be mixture of positives , negatives and zeros

Repetition of numbers in the array/list could occur.



Input >> Output Examples
maxProduct ({4, 3, 5}, 2) ==>  return (20)
Explanation:
Since the size (k) equal 2 , then the subsequence of size 2 whose gives product of maxima  is 5 * 4 = 20 .


maxProduct ({8, 10 , 9, 7}, 3) ==>  return (720)
Explanation:
Since the size (k) equal 3 , then the subsequence of size 3 whose gives product of maxima  is 8 * 9 * 10 = 720 .


maxProduct ({10, 8, 3, 2, 1, 4, 10}, 5) ==> return (9600)
Explanation:
Since the size (k) equal 5 , then the subsequence of size 5 whose gives product of maxima  is 10 * 10 * 8 * 4 * 3 = 9600

maxProduct ({-4, -27, -15, -6, -1}, 2) ==> return (4)
Explanation:
Since the size (k) equal 2 , then the subsequence of size 2 whose gives product of maxima  is -4 * -1 = 4 .

maxProduct ({10, 3, -1, -27} , 3)  return (-30)
Explanation:
Since the size (k) equal 3 , then the subsequence of size 3 whose gives product of maxima  is 10 * 3 * -1 = -30 .


Playing with Numbers Series
Playing With Lists/Arrays Series
For More Enjoyable Katas

ALL translations are welcomed
Enjoy Learning !!
Zizou
"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def max_product(lst, n_largest_elements):
    import numpy
    return numpy.prod(sorted(lst)[-n_largest_elements:])

# ---------------  TEST CASES ---------------
test.it("Basic Tests")
test.assert_equals(max_product([0]*10, 5), 0)
test.assert_equals(max_product([4,3,5], 2), 20)
test.assert_equals(max_product([10,8,7,9], 3), 720)
test.assert_equals(max_product([8,6,4,6], 3), 288)

test.it("Larger arrays")
test.assert_equals(max_product (list(range(10, -1, -1)), 5), 10*9*8*7*6)
test.assert_equals(max_product ([10,2,3,8,1,10,4], 5), 9600)
test.assert_equals(max_product ([13,12,-27,-302,25,37,133,155,-1], 5), 247895375)
             
test.it("Arrays with negative values")
test.assert_equals(max_product ([-4,-27,-15,-6,-1],2), 4)
test.assert_equals(max_product ([-17,-8,-102,-309],2), 136)
             
test.it("Arrays with positive and negative values")
test.assert_equals(max_product ([10,3,-27,-1], 3), -30)
