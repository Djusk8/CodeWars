# ------------  KATA DESCRIPTION ------------
"""
6 kyu Almost Even

We need the ability to divide an unknown integer into a given number of even parts — or at least as even as they can be. The sum of the parts should be the original value, but each part should be an integer, and they should be as close as possible.

Example code:

split_integer(20, 6)  # returns [3, 3, 3, 3, 4, 4]

Complete the function so that it returns an array of integer representing the parts. Ignoring the order of the parts, there is only one valid solution for each input to your function!

(Also, there is no reason to test for edge cases: the input to your function will always be valid for this kata.)

"""

# ---------------  SOLUTION ---------------
import codewars_test as test


def split_integer(num, parts):

    # first solution
    # return sorted(num // parts if i >= num % parts else num // parts+1 for i in range(parts))

    # better and faster solution
    return [num // parts]*(parts - num % parts) + [num // parts + 1]*(num % parts)



# ---------------  TEST CASES ---------------
test.assert_equals(split_integer(10, 1), [10])
test.assert_equals(split_integer(2, 2), [1, 1])
test.assert_equals(split_integer(20, 5), [4, 4, 4, 4, 4])