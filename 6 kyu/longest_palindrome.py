# ------------  KATA DESCRIPTION ------------
"""
6 kyu
Longest Palindrome

Find the length of the longest substring in the given string s that is the same in reverse.

As an example, if the input was “I like racecars that go fast”, the substring (racecar) length would be 7.

If the length of the input string is 0, the return value must be 0.
Example:

"a" -> 1
"aab" -> 2
"abcde" -> 1
"zzbaabcd" -> 4
"" -> 0
"""

# ---------------  SOLUTION ---------------
import codewars_test as test


def longest_palindrome(s):
    ln = 0

    for i in range(len(s)):
        for j in range(len(s) - i):
            st = s[i:j + i + 1]
            if st == st[::-1]:
                ln = max(ln, len(s[i:i + j + 1]))
    return ln


# ---------------  TEST CASES ---------------
test.assert_equals(longest_palindrome("a"), 1)
test.assert_equals(longest_palindrome("aa"), 2)
test.assert_equals(longest_palindrome("baa"), 2)
test.assert_equals(longest_palindrome("aab"), 2)
test.assert_equals(longest_palindrome("abcdefghba"), 1)
test.assert_equals(longest_palindrome("baablkj12345432133d"), 9)
