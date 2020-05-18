# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/52dbae61ca039685460001ae

7 kyu - Search for letters

Create a function which accepts one arbitrary string as an argument, and return a string of length 26.
The objective is to set each of the 26 characters of the output string to either '1' or '0' based on the fact whether
the Nth letter of the alphabet is present in the input (independent of its case).
So if an 'a' or an 'A' appears anywhere in the input string (any number of times), set the first character of the output
string to '1', otherwise to '0'. if 'b' or 'B' appears in the string, set the second character to '1', and so on for the
rest of the alphabet.
For instance:
"a   **&  cZ"  =>  "10100000000000000000000001"""

# ---------------  SOLUTION ---------------
import codewars_test as test


def change(st):
    result = ['0'] * 26
    for i in set(st.lower()):
        if i.isalpha():
            result[ord(i) - 97] = '1'
    return ''.join(result)


# ---------------  TEST CASES ---------------
@test.describe('Example Tests')
def example_tests():
    test.assert_equals(change("a **&  bZ"), "11000000000000000000000001")
    test.assert_equals(change('Abc e  $$  z'), "11101000000000000000000001")
    test.assert_equals(change("!!a$%&RgTT"), "10000010000000000101000000")
    test.assert_equals(change(""), "00000000000000000000000000", "empty string should return 26 '0'")
    test.assert_equals(change("abcdefghijklmnopqrstuvwxyz"), "11111111111111111111111111")
    test.assert_equals(change("aaaaaaaaaaa"), "10000000000000000000000000")
    test.assert_equals(change("&%&%/$%$%$%$%GYtf67fg34678hgfdyd"), "00010111000000000001000010")
