# ------------  KATA DESCRIPTION ------------
"""
7 kyu - Help Bob count letters and digits.

Bob is a lazy man.

He needs you to create a method that can determine how many letters and digits are in a given string.

Example:

"hel2!lo" --> 6

"wicked .. !" --> 6

"!?..A" --> 1


"""

# ---------------  SOLUTION ---------------
import codewars_test as Test


def count_letters_and_digits(s):
    import re
    return len(re.findall(r'[a-zA-Z0-9]', s))


# ---------------  TEST CASES ---------------
Test.it('Basic tests')
Test.assert_equals(count_letters_and_digits('n!!ice!!123'), 7)
Test.assert_equals(count_letters_and_digits('de?=?=tttes!!t'), 8)
Test.assert_equals(count_letters_and_digits(''), 0)
Test.assert_equals(count_letters_and_digits('!@#$%^&`~.'), 0)
Test.assert_equals(count_letters_and_digits('u_n_d_e_r__S_C_O_R_E'), 10)