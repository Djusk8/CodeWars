# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/57e3f79c9cb119374600046b

8 kyu - Hello, Name or World!

Define a method hello that returns "Hello, Name!" to a given name, or says Hello, World! if name is not given (or passed
as an empty String).
Assuming that name is a String and it checks for user typos to return a name with a first capital letter (Xxxx).
Examples:

hello "john"   => "Hello, John!"
hello "aliCE"  => "Hello, Alice!"
hello          => "Hello, World!" # name not given
hello ''       => "Hello, World!" # name is an empty String


"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def hello(name=None):
    return f"Hello, {name.capitalize()}!" if name else "Hello, World!"


# ---------------  TEST CASES ---------------
test.describe("Example Tests")

tests = (
    ("John", "Hello, John!"),
    ("aLIce", "Hello, Alice!"),
    ("", "Hello, World!"),
)

for inp, exp in tests:
    test.assert_equals(hello(inp), exp)

test.assert_equals(hello(), "Hello, World!")
