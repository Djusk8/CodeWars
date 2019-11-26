# ------------  KATA DESCRIPTION ------------
"""
8 kyu - MakeUpperCase

Write function makeUpperCase.
"""

# ---------------  SOLUTION ---------------
import codewars_test as test


def make_upper_case(s):
    return "".join([chr(ord(x) - 32) if ord(x) in range(97, 123) else x for x in s])


# ---------------  TEST CASES ---------------
test.describe("Final Tests")
test.assert_equals(make_upper_case("hello"), "HELLO")
test.assert_equals(make_upper_case("hello world"), "HELLO WORLD")
test.assert_equals(make_upper_case("hello world !"), "HELLO WORLD !")
test.assert_equals(make_upper_case("heLlO wORLd !"), "HELLO WORLD !")
test.assert_equals(make_upper_case("1,2,3 hello world!"), "1,2,3 HELLO WORLD!")
import random
letters = "abcdefgh ijklmnopq rstuvwxyz ABCDEFGHIJ QLMNOPQRSTUVWXYZ 1234567890!"
for cwtests in range(0,95):
    word = ""
    for l in range(0,random.randint(1,99)):
        word += letters[random.randint(0,len(letters)-1)]
    test.assert_equals(make_upper_case(word), word.upper())