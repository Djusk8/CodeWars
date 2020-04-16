# ------------  KATA DESCRIPTION ------------
"""
7 kyu
My Languages

Your task

You are given a dictionary/hash/object containing some languages and your test results in the given languages.
Return the list of languages where your test score is at least 60, in descending order of the results.

Note: the scores will always be unique (so no duplicate values)
Examples

{"Java": 10, "Ruby": 80, "Python": 65}    -->  ["Ruby", "Python"]
{"Hindi": 60, "Dutch" : 93, "Greek": 71}  -->  ["Dutch", "Greek", "Hindi"]
{"C++": 50, "ASM": 10, "Haskell": 20}     -->  []
"""

# ---------------  SOLUTION ---------------
import codewars_test as Test


def my_languages(results):
    return sorted([r for r in results if results[r] >= 60], key=results.__getitem__, reverse=True)


# ---------------  TEST CASES ---------------
Test.assert_equals(my_languages({"Java": 10, "Ruby": 80, "Python": 65}), ["Ruby", "Python"])
Test.assert_equals(my_languages({"Hindi": 60, "Dutch": 93, "Greek": 71}), ["Dutch", "Greek", "Hindi"])
Test.assert_equals(my_languages({"C++": 50, "ASM": 10, "Haskell": 20}), [])