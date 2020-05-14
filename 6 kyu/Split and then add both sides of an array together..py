# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/5946a0a64a2c5b596500019a

6 kyu - Split and then add both sides of an array together.

Inspired by the Fold an Array kata. This one is sort of similar but a little different.

Task
You will receive an array as parameter that contains 1 or more integers and a number n.
Here is a little visualization of the process:

Step 1: Split the array in two:
{1, 2, 5, 7, 2, 3, 5, 7, 8}
      /            \
{1, 2, 5, 7}    {2, 3, 5, 7, 8}
Step 2: Put the arrays on top of each other:
   {1, 2, 5, 7}
{2, 3, 5, 7, 8}
Step 3: Add them together:
{2, 4, 7, 12, 15}

Repeat the above steps n times or until there is only one number left, and then return the array.
Example
Input: {4, 2, 5, 3, 2, 5, 7}, n=2


Round 1
-------
step 1: {4, 2, 5}  {3, 2, 5, 7}

step 2:    {4, 2, 5}
        {3, 2, 5, 7}

step 3: {3, 6, 7, 12}


Round 2
-------
step 1: {3, 6}  {7, 12}

step 2:  {3,  6}
         {7, 12}

step 3: {10, 18}


Result: {10, 18}"""


# ---------------  SOLUTION ---------------
import codewars_test as test
from itertools import zip_longest


def split_and_add(numbers, n):
    if len(numbers) == 1 or not n:
        return numbers
    else:
        ln = len(numbers)//2-1
        a, b = numbers[:ln:-1], numbers[ln::-1]
        c = [sum(i) for i in zip_longest(a, b, fillvalue=0)][::-1]
        return split_and_add(c, n-1)

# ---------------  TEST CASES ---------------
test.assert_equals(split_and_add([1,2,3,4,5], 2), [5,10])
test.assert_equals(split_and_add([1,2,3,4,5], 3), [15])
test.assert_equals(split_and_add([15], 3), [15])
test.assert_equals(split_and_add([32,45,43,23,54,23,54,34], 2), [183, 125])
test.assert_equals(split_and_add([32,45,43,23,54,23,54,34], 0), [32,45,43,23,54,23,54,34])
test.assert_equals(split_and_add([3,234,25,345,45,34,234,235,345], 3), [305, 1195])
test.assert_equals(split_and_add([3,234,25,345,45,34,234,235,345,34,534,45,645,645,645,4656,45,3], 4), [1040, 7712])
test.assert_equals(split_and_add([23,345,345,345,34536,567,568,6,34536,54,7546,456], 20), [79327])
