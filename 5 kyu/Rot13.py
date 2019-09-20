# ------------  KATA DESCRIPTION ------------
"""
5 kyu
Rot13

ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.

"""

# ---------------  SOLUTION ---------------
import codewars_test as test

from string import ascii_lowercase, ascii_uppercase

lower = ascii_lowercase * 2
upper = ascii_uppercase * 2


def rot13(message):
    new_string = str()

    for char in message:

        if char.isupper():
            new_string += upper[upper.index(char) + 13]
        elif char.islower():
            new_string += lower[lower.index(char) + 13]
        else:
            new_string += char

    return new_string


# ---------------  TEST CASES ---------------
test.assert_equals(rot13("test"),"grfg")
test.assert_equals(rot13("Test"),"Grfg")