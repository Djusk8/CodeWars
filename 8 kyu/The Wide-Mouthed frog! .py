# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/57ec8bd8f670e9a47a000f89

8 kyu - The Wide-Mouthed frog! 

The wide mouth frog is particularly interested in the eating habits of other creatures.
He just can't stop asking the creatures he encounters what they like to eat. But then he meet the alligator who just
LOVES to eat wide-mouthed frogs!
When he meets the alligator, it then makes a tiny mouth.
Your goal in this kata is to create complete the mouth_size method this method take one argument animal which
corresponds to the animal encountered by frog. If this one is an alligator (case insensitive) return small otherwise
return wide.

"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def mouth_size(animal): 
    # v1
    return "small" if animal.lower() == "alligator" else "wide"
    # v2
    # return ["wide", "small"][animal.lower() == "alligator"]


# ---------------  TEST CASES ---------------
test.describe("Basic Tests")
test.assert_equals(mouth_size("toucan"),"wide")
test.assert_equals(mouth_size("ant bear"),"wide")
test.assert_equals(mouth_size("alligator"),"small")

