# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/53573877d5493b4d6e00050c

7 kyu - Find the Capitals

Write a method that takes a sequence of objects with two keys each: country or state, and capital. Keys may be symbols
or strings
The method should return an array of sentences declaring the state or country and its capital.
Examples
[{'state': 'Maine', 'capital': 'Augusta'}] --> ["The capital of Maine is Augusta"]
[{'country' : 'Spain', 'capital' : 'Madrid'}] --> ["The capital of Spain is Madrid"]
[{"state" : 'Maine', 'capital': 'Augusta'}, {'country': 'Spain', "capital" : "Madrid"}] --> ["The capital of Maine is
Augusta", "The capital of Spain is Madrid"]
"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def capital(capitals): 
    return [f"The capital of {i['state'] if 'state' in i else i['country']} is {i['capital']}" for i in capitals]


# ---------------  TEST CASES ---------------
@test.describe('Example Tests')
def example_tests():
    state_capitals = [{'state': 'Maine', 'capital': 'Augusta'}]
    test.assert_equals(capital(state_capitals), ["The capital of Maine is Augusta"]);
    
    country_capitals = [{'country' : 'Spain', 'capital' : 'Madrid'}]
    test.assert_equals(capital(country_capitals), ["The capital of Spain is Madrid"])
    
    mixed_capitals = [{"state" : 'Maine', 'capital': 'Augusta'}, {'country': 'Spain', "capital" : "Madrid"}]
    test.assert_equals(capital(mixed_capitals), ["The capital of Maine is Augusta", "The capital of Spain is Madrid"])
