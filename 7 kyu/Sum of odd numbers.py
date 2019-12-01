# ------------  KATA DESCRIPTION ------------
"""
7 kyu - Sum of odd numbers

Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...

Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:

row_sum_odd_numbers(1); # 1
row_sum_odd_numbers(2); # 3 + 5 = 8

"""

# ---------------  SOLUTION ---------------
import codewars_test as Test

# While this cata has mathematical solution I wanted find programming solution


def calc_first_row_num(lvl):
    if lvl == 1:
        return 0
    else:
        return lvl - 1 + calc_first_row_num(lvl-1)


def row_sum_odd_numbers(n):
    first_row_num = calc_first_row_num(n)
    return sum([1 + 2 * (first_row_num + i) for i in range(n)])


# ---------------  TEST CASES ---------------
Test.assert_equals(row_sum_odd_numbers(1), 1)
Test.assert_equals(row_sum_odd_numbers(2), 8)
Test.assert_equals(row_sum_odd_numbers(13), 2197)
Test.assert_equals(row_sum_odd_numbers(19), 6859)
Test.assert_equals(row_sum_odd_numbers(41), 68921)