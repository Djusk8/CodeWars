# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/5704aea738428f4d30000914

8 kyu - Triple Trouble

Triple Trouble
Create a function that will return a string that combines all of the letters of the three inputed strings in groups.
Taking the first letter of all of the inputs and grouping them next to each other.  Do this for every letter, see
example below!
E.g. Input: "aa", "bb" , "cc" => Output: "abcabc"
Note: You can expect all of the inputs to be the same length.
"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def triple_trouble(one, two, three):
    return ''.join(a+b+c for a, b, c in zip(one, two, three))


# ---------------  TEST CASES ---------------
test.describe("Basic tests")
test.assert_equals(triple_trouble("aaa","bbb","ccc"), "abcabcabc")
test.assert_equals(triple_trouble("aaaaaa","bbbbbb","cccccc"), "abcabcabcabcabcabc")
test.assert_equals(triple_trouble("burn", "reds", "roll"), "brrueordlnsl")
test.assert_equals(triple_trouble("Bm", "aa", "tn"), "Batman")
test.assert_equals(triple_trouble("LLh", "euo", "xtr"), "LexLuthor")
