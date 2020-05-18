# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/57a6633153ba33189e000074

7 kyu - Ordered Count of Characters

Count the number of occurrences of each character and return it as a list of tuples in order of appearance. For empty
output return an empty list.
Example:
ordered_count("abracadabra") == [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]
"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def ordered_count(inp):
    return [(i, inp.count(i)) for i in list(dict.fromkeys(inp))]

# ---------------  TEST CASES ---------------
test.describe("Basic Tests")

tests = (
    ('abracadabra', [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]),
    ('Code Wars', [('C', 1), ('o', 1), ('d', 1), ('e', 1), (' ', 1), ('W', 1), ('a', 1), ('r', 1), ('s', 1)])
)

for t in tests:
    inp, exp = t
    test.assert_equals(ordered_count(inp), exp)
