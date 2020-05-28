# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/56f173a35b91399a05000cb7

8 kyu - Squash the bugs

Simple challenge - eliminate all bugs from the supplied code so that the code runs and outputs the expected value.
Output should be the length of the longest word, as a number.
There will only be one 'longest' word.
"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def find_longest(string):
    spl = string.split(" ")
    longest = 0
    i = 0
    while i < len(spl):
        if len(spl[i]) > longest:
            longest = len(spl[i])
        i += 1
    return longest


# ---------------  TEST CASES ---------------
test.describe("Basic tests")
test.assert_equals(find_longest("The quick white fox jumped around the massive dog"), 7)
test.assert_equals(find_longest("Take me to tinseltown with you"), 10)
test.assert_equals(find_longest("Sausage chops"), 7)
test.assert_equals(find_longest("Wind your body and wiggle your belly"), 6)
test.assert_equals(find_longest("Lets all go on holiday"), 7)
