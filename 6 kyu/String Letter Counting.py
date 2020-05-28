# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/59e19a747905df23cb000024

6 kyu - String Letter Counting

Take an input string and return a string that is made up of the number of occurances of each english letter in the
input, followed by that letter. The string shouldn't contain zeros; leave them out.
An empty string, or one with no letters, should return an empty string.
Notes:

the input will always be valid;
treat letters as case-insensitive

Examples
"This is a test sentence."  ==>  "1a1c4e1h2i2n4s4t"
""                          ==>  ""
"555"                       ==>  """""


# ---------------  SOLUTION ---------------
import codewars_test as test


def string_letter_count(s):
    return ''.join(str(s.lower().count(l))+l for l in sorted(list(set(s.lower()))) if l.isalpha())


# ---------------  TEST CASES ---------------
test.assert_equals(string_letter_count("The quick brown fox jumps over the lazy dog."), "1a1b1c1d3e1f1g2h1i1j1k1l1m1n4o1p1q2r1s2t2u1v1w1x1y1z")
test.assert_equals(string_letter_count("The time you enjoy wasting is not wasted time."), "2a1d5e1g1h4i1j2m3n3o3s6t1u2w2y")
test.assert_equals(string_letter_count("./4592#{}()"), "")
