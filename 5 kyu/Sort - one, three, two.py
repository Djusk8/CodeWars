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

number_system = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
}


def n2w(num: int) -> str:
    """ Convert int number to its word representation """
    x = str()

    # return zero if number is 0
    # if num == 0:
    #     return number_system[num]

    # if number greater than 100 add it's hundred's part words
    if num >= 100:
        x += number_system[num // 100] + " hundred"

        # if there are tenth and\or one's in the numbers add word 'and'
        if num % 100:
            x += ' and '

        # remove hundred's part from number
        num = num % 100

    # convert tenths from 20 to 90
    if num in range(20, 100):
        x += number_system[num // 10 * 10]
        if num % 10:
            x += '-'
        num = num % 10

    # for numbers from 10 to 19 use special words and return the result
    if num in range(0, 20):
        x += number_system[num]
        return x

    # # finally convert the one's
    # if num:
    #     x += number_system[num]

    return x


def sort_by_name(nums):

    nums_str = sorted([(n2w(n), n) for n in nums])  # Convert list of numbers to list of (word, num) and sort it by name
    return [n[1] for n in nums_str]  # Extract list of numbers from sorted list of words


# ---------------  TEST CASES ---------------
Test.assert_equals(sort_by_name([8, 8, 9, 9, 10, 10]), [8, 8, 9, 9, 10, 10])
Test.assert_equals(sort_by_name([1, 2, 3, 4]), [4, 1, 3, 2])
Test.assert_equals(sort_by_name([9, 99, 999]), [9, 999, 99])