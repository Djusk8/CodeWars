# ------------  KATA DESCRIPTION ------------
"""
8 kyu
Abbreviate a Two Word Name

Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

Patrick Feeney => P.F


"""

# ---------------  SOLUTION ---------------
import codewars_test as Test


def abbrevName(name):
    return '.'.join(x[0].upper() for x in name.split())


# ---------------  TEST CASES ---------------
Test.assert_equals(abbrevName("Sam Harris"), "S.H");
Test.assert_equals(abbrevName("Patrick Feenan"), "P.F");
Test.assert_equals(abbrevName("Evan Cole"), "E.C");
Test.assert_equals(abbrevName("P Favuzzi"), "P.F");
Test.assert_equals(abbrevName("David Mendieta"), "D.M");