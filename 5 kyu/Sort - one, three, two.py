# ------------  KATA DESCRIPTION ------------
"""
5 kyu
Sort - one, three, two

Hey You !

Sort these integers for me ...

By name ...

Do it now !
Input

    Range is 0-999

    There may be duplicates

    The array may be empty
"""

# ---------------  SOLUTION ---------------
import codewars_test as Test

# While the main purpose of any code-education platform is to write code, I think the right approach to solve any catas
# is to write as much code as possible, avoiding the use of third-party libraries.
# So it will be more useful to code your own functions instead of num2words and word2number.
# I plan to update solution with my own libraries later

from num2words import num2words
from word2number import w2n


def sort_by_name(nums):

    nums_str = sorted([num2words(n) for n in nums])     # Convert list of numbers to words list and sort it by name
    return [w2n.word_to_num(n) for n in nums_str]       # Convert sorted list of words to numbers


# ---------------  TEST CASES ---------------
Test.assert_equals(sort_by_name([8, 8, 9, 9, 10, 10]), [8, 8, 9, 9, 10, 10])
Test.assert_equals(sort_by_name([1, 2, 3, 4]), [4, 1, 3, 2])
Test.assert_equals(sort_by_name([9, 99, 999]), [9, 999, 99])