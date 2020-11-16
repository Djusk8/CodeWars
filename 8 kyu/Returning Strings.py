# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/55a70521798b14d4750000a4

8 kyu - Returning Strings

Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how
are you doing today?".
[Make sure you type the exact thing I wrote or the program may not execute properly]

"""

# ---------------  SOLUTION ---------------
import codewars_test as test

greet = lambda name: f"Hello, {name} how are you doing today?"

# ---------------  TEST CASES ---------------
test.assert_equals(greet('Ryan'), "Hello, Ryan how are you doing today?")
