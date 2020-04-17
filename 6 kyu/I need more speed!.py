# ------------  KATA DESCRIPTION ------------
"""
6 kyu
I need more speed!

Write a function that will take in any array and reverse it.

Sounds simple doesn't it?

NOTES:

    Array should be reversed in place! (no need to return it)
    Usual builtins have been deactivated. Don't count on them.
    You'll have to do it fast enough, so think about performances

"""

# ---------------  SOLUTION ---------------
import codewars_test as test


"""
Remove this comment otherwise your code cannot pass the anti-cheat tests!

You are not allowed to use the following:
    - python 2
    - slice notations
    - defining an empty list: []. Use "x=list()" instead if you need it
    - list comprehensions
    - the spread operator inside square brackets
    - "tuple" and "reversed" builtins have been deactivated

The "list" builtin has been replaced with another implementation with the following specifications:
    - list.reverse is forbidden
    - list.__reversed__ is forbidden
    - slicing is forbidden
All other usual methods of the list class are still present.
"""


def reverse(seq):
    for i in range(len(seq)//2):
        seq[i], seq[len(seq)-1-i] = seq[len(seq)-1-i], seq[i]


# ---------------  TEST CASES ---------------
@test.describe('Example Tests')
def example_tests():
    seq = [1, 2, 3, 4, 5]
    reverse(seq)
    test.assert_equals([5, 4, 3, 2, 1], seq)

    seq = ['?', 'you', 'are', 'how', 'world', 'hello']
    reverse(seq)
    test.assert_equals(['hello', 'world', 'how', 'are', 'you', '?'], seq)

    seq = [{'b': 2}, {'a': 1}]
    reverse(seq)
    test.assert_equals([{'a': 1}, {'b': 2}], seq)