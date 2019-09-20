# ------------  KATA DESCRIPTION ------------
"""
Write Number in Expanded Form

You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'

NOTE: All numbers will be whole numbers greater than 0.
"""

# ---------------  SOLUTION ---------------
import codewars_test as test


def expanded_form(num):
    #     v1 one string solution
    #     return " + ".join(reversed([str(int(dig) * 10 ** i) for i, dig in enumerate(reversed(str(num))) if int(dig)]))

    #     v2 human readable solution
    string = str(num)
    eform = [str(int(dig) * 10 ** (len(string) - i - 1)) for i, dig in enumerate(string) if int(dig)]
    return " + ".join(eform)


# ---------------  TEST CASES ---------------
test.assert_equals(expanded_form(12), '10 + 2');
test.assert_equals(expanded_form(42), '40 + 2');
test.assert_equals(expanded_form(70304), '70000 + 300 + 4');