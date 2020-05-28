# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/535474308bb336c9980006f2

7 kyu - Greet Me

Write a method that takes one argument as name and then greets that name, capitalized and ends with an exclamation
point.
Example:
"riley" --> "Hello Riley!"
"JACK"  --> "Hello Jack!"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def greet(name): 
    return "Hello {}!".format(name.capitalize())


# ---------------  TEST CASES ---------------
@test.describe('Example Tests')
def example_tests():
    test.assert_equals(greet('riley'), 'Hello Riley!')
    test.assert_equals(greet('molly'), "Hello Molly!")
    test.assert_equals(greet('BILLY'), "Hello Billy!")
