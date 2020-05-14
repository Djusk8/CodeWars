# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/5d50e3914861a500121e1958

7 kyu - Alphabetical Addition

Your task is to add up letters to one letter.
The function will be given a variable amount of arguments, each one being a letter to add.
Notes:

Letters will always be lowercase.
Letters can overflow (see second to last example of the description)
If no letters are given, the function should return 'z'

Examples:
add_letters('a', 'b', 'c') = 'f'
add_letters('a', 'b') = 'c'
add_letters('z') = 'z'
add_letters('z', 'a') = 'a'
add_letters('y', 'c', 'b') = 'd' # notice the letters overflowing
add_letters() = 'z'
Confused? Roll your mouse/tap over here
"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def add_letters(*letters):
    import string
    return string.ascii_lowercase[sum(ord(ltr)-96 for ltr in letters) % 26 - 1]


# ---------------  TEST CASES ---------------
@test.describe("Fixed tests")
def fixed_tests():
    tests = [
        (['a', 'b', 'c'], 'f'),
        (['z'], 'z'),
        (['a', 'b'], 'c'),
        (['c'], 'c'),
        (['z', 'a'], 'a'),
        (['y', 'c', 'b'], 'd'),
        ([], 'z')
    ]
    for i, o in tests:
        str = ', '.join(['"' + s + '"' for s in i])
        @test.it("add_letters(" + str + ")")
        def fixed_test():
            test.assert_equals(add_letters(*i), o)
