# ------------  KATA DESCRIPTION ------------
"""
5 kyu - Pete, the baker

Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. Can you help him to find out, how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.

Examples:

# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000}
"""

# ---------------  SOLUTION ---------------
import codewars_test as test


def cakes(recipe, available):

    mn = float('inf')  # used to store minimum, initialized with positive infinity

    for ing in recipe:
        if ing in available:  # find how many cakes you can bake for that ingredient and save minimum amount
            mn = min(mn, available[ing] // recipe[ing])
        else:
            return 0  # if there is no ingredient available no cakes can be baked

    return mn


# ---------------  TEST CASES ---------------
test.describe('Testing Pete, the Baker')
test.it('gives us the right number of cakes')

recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
test.assert_equals(cakes(recipe, available), 2, 'Wrong result for example #1')

recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}
test.assert_equals(cakes(recipe, available), 0, 'Wrong result for example #2')