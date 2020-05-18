# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/523b4ff7adca849afe000035

8 kyu - Function 1 - hello world

Description:
Make a simple function called greet that returns the most-famous "hello world!".
Style Points
Sure, this is about as easy as it gets. But how clever can you be to create the most creative hello world you can think
of? What is a "hello world" solution you would want to show your friends?
"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def greet():
    return "hello world!"


# ---------------  TEST CASES ---------------
test.describe("Greet function")
test.it("Making sure greet exists")
test.assert_equals(greet(), "hello world!", "Greet doesn't return hello world!")
