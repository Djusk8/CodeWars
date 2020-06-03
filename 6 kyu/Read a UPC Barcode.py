# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/5b7dfd8cbfae24e5f200004d

6 kyu - Read a UPC/Barcode


Your task is to convert a string representing the lines/spaces in a 12 digit barcode/UPC-A into a string of numbers 0-9.
A black line represents a 1 and a space represents 0. The string you are returning is the decimal representation of
those binary digits. NOTE: The digits 0-9 are not represented as bits the usual way, UPC has it's own tables which are
preloaded as LEFT_HAND and RIGHT_HAND dictionaries.
The LEFT_HAND and RIGHT_HAND dictionaries contain 7 digit bit strings as keys and an integer for values. For example:
'0011001' = 1 in LEFT_HAND
'1100110' = 1 in RIGHT_HAND, left and right side bit strings are complements of each other.
The structure of a UPC-A is as follows:

Starts with a guard pattern, always representing 101. Known as left-hand guard pattern.
6 groups of 7 bits each, eg: '  ▍▍  ▍' = '0011001' = 1(left-hand). The first group is the number system digit.
A center guard pattern, always representing 01010. Divides "left-hand" groups and "right-hand" groups.
6 groups of 7 bits each, eg: '▍▍  ▍▍ ' = '1100110' = 1(right-hand). The last group is the modulo check digit.
Ends with a guard pattern, always representing 101. Known as right-hand guard pattern.

The format for your returned string is:
'(number_system) (left_hand) (right_hand) (modulo_check)'
Example barcode, sorry about number formatting:
1. '▍ ▍   ▍▍ ▍ ▍▍   ▍  ▍▍  ▍   ▍▍ ▍   ▍▍ ▍   ▍▍ ▍ ▍ ▍ ▍▍▍  ▍ ▍▍  ▍▍ ▍▍ ▍▍  ▍  ▍▍▍ ▍▍  ▍▍ ▍   ▍  ▍ ▍'
2. '(101)0001101,0110001,0011001,0001101,0001101,0001101(01010)1110010,1100110,1101100,1001110,1100110,1000100(101)'
3. (left_guard)0,5,1,0,0,0(center_guard)0,1,2,5,1,7(right_guard)
return '0 51000 01251 7'
For this kata there will be no tricks, no error checking, or reading backwards. Inputs will always be correct, left to
right, and a single bar/space will always represent 1/0. The validity of modulo check digit is irrelevant here, we're
just doing conversion and formatting. Guards are not part of the returned string but will be part of the input.
A bar in case you need to use it: ▍
Further reading/details wiki, thanks to CODE by Charles Petzold.

"""


# ---------------  SOLUTION ---------------
import codewars_test as test
import re

LEFT_HAND = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}
RIGHT_HAND = {'1110010': 0, '1100110': 1, '1101100': 2, '1000010': 3, '1011100': 4, '1001110': 5, '1010000': 6, '1000100': 7, '1001000': 8, '1110100': 9}


def read_barcode(barcode):
    # convert the string to binary view
    barcode = barcode.translate(str.maketrans('▍ ', "10"))

    # find left_hand (lh) and right_hand (rh) groups
    pattern = r"101(\d{42})01010(\d{42})101$"
    x = re.search(pattern, barcode)
    lh = re.findall(r'\d{7}', x.group(1))
    rh = re.findall(r'\d{7}', x.group(2))

    # convert binary to int digits
    lh = [str(LEFT_HAND[p]) for p in lh]
    rh = [str(RIGHT_HAND[p]) for p in rh]

    # format and return the result
    return f"{lh[0]} {''.join(lh[1:])} {''.join(rh[:-1])} {rh[-1]}"


# ---------------  TEST CASES ---------------
test.describe('should convert barcode to digits')

test.it("Campbell's Chicken Noodle Soup")
test.assert_equals(read_barcode('▍ ▍   ▍▍ ▍ ▍▍   ▍  ▍▍  ▍   ▍▍ ▍   ▍▍ ▍   ▍▍ ▍ ▍ ▍ ▍▍▍  ▍ ▍▍  ▍▍ ▍▍ ▍▍  ▍  ▍▍▍ ▍▍  ▍▍ ▍   ▍  ▍ ▍'), '0 51000 01251 7')

test.it("Hershey's Natural Unsweetened Cocoa")
test.assert_equals(read_barcode('▍ ▍   ▍▍ ▍ ▍▍▍▍ ▍ ▍   ▍▍   ▍▍ ▍   ▍▍ ▍   ▍▍ ▍ ▍ ▍ ▍▍▍  ▍ ▍  ▍▍▍ ▍▍ ▍▍  ▍▍▍  ▍ ▍▍▍  ▍ ▍ ▍▍▍  ▍ ▍'), '0 34000 05200 4')

test.it("Bob's Red Mill Corn Grits")
test.assert_equals(read_barcode('▍ ▍   ▍▍ ▍ ▍▍▍▍ ▍   ▍ ▍▍   ▍ ▍▍ ▍▍▍ ▍▍ ▍▍ ▍▍▍ ▍ ▍ ▍▍▍  ▍ ▍▍▍  ▍ ▍▍  ▍▍ ▍▍ ▍▍  ▍  ▍▍▍ ▍▍ ▍▍  ▍ ▍'), '0 39978 00125 2')

test.it("Dutch Gold Pure Buckwheat Honey ")
test.assert_equals(read_barcode('▍ ▍   ▍▍ ▍ ▍▍▍ ▍▍ ▍▍▍▍ ▍  ▍▍  ▍ ▍▍▍▍ ▍ ▍▍ ▍▍▍ ▍ ▍ ▍▍ ▍▍  ▍▍▍  ▍ ▍ ▍▍▍  ▍▍  ▍▍ ▍▍▍  ▍ ▍   ▍  ▍ ▍'), '0 73138 20410 7')

test.it("Black Bear Spicy Brown Mustard")
test.assert_equals(read_barcode('▍ ▍ ▍ ▍▍▍▍ ▍▍▍▍ ▍   ▍▍ ▍   ▍▍ ▍   ▍▍ ▍ ▍▍▍▍ ▍ ▍ ▍ ▍▍▍ ▍  ▍▍  ▍▍ ▍ ▍▍▍  ▍  ▍▍▍ ▍  ▍▍▍ ▍ ▍    ▍ ▍'), '6 30003 91455 6')

test.it("Barilla Fideo Cut Spaghetti Pasta")
