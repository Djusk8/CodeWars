# ------------  KATA DESCRIPTION ------------
"""
8 kyu - Convert a string to an array

Write a function to split a string and convert it into an array of words. For example:

"Robin Singh" ==> ["Robin", "Singh"]

"I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]
"""

# ---------------  SOLUTION ---------------
import codewars_test as Test

# while s.split(" ") is the easiest solution with build0in functions, I want to get some practice and write my own func
# to split a string


def string_to_array(s):
    result = []
    tmp = ""

    for ch in s:
        if ch == " ":
            result.append(tmp)
            tmp = ""
        else:
            tmp += ch

    result.append(tmp)  # add to result the last word in string

    return result


# ---------------  TEST CASES ---------------
Test.describe("Basic tests")
Test.assert_equals(string_to_array("Robin Singh"), ["Robin", "Singh"])
Test.assert_equals(string_to_array("CodeWars"), ["CodeWars"])
Test.assert_equals(string_to_array("I love arrays they are my favorite"), ["I", "love", "arrays", "they", "are", "my", "favorite"])
Test.assert_equals(string_to_array("1 2 3"), ["1", "2", "3"])
Test.assert_equals(string_to_array(""), [""])

Test.describe("Random tests")
from random import randint
sol=lambda s: s.split(" ")
base="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

for _ in range(40):
    s=" ".join(["".join([base[randint(0,len(base)-1)] for q in range(randint(1,20))]) for k in range(randint(1,15))])
    Test.it("Testing for "+repr(s))
    Test.assert_equals(string_to_array(s),sol(s),"It should work for random inputs too")