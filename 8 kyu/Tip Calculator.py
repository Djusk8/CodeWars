# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/56598d8076ee7a0759000087

8 kyu - Tip Calculator

Complete the function, which calculates how much you need to tip based on the total amount of the bill and the service.
You need to consider the following ratings:

Terrible: tip 0%
Poor: tip 5%
Good: tip 10%
Great: tip 15%
Excellent: tip 20%

The rating is case insensitive (so "great" = "GREAT"). If an unrecognised rating is received, then you need to return:

"Rating not recognised" in Javascript, Python and Ruby...
...or null in Java
...or -1 in C#

Because you're a nice person, you always round up the tip, regardless of the service.

"""


# ---------------  SOLUTION ---------------
import codewars_test as test
import math
data = {"terrible":  0, "poor":  5, "good":  10, "great":  15, "excellent":  20}


def calculate_tip(amount, rating):
    try:
        tip = data[rating.lower()]
    except:
        return "Rating not recognised"
    return math.ceil(amount * tip / 100)


# ---------------  TEST CASES ---------------
test.assert_equals(calculate_tip(30, "poor"), 2)
test.assert_equals(calculate_tip(20, "Excellent"), 4)
test.assert_equals(calculate_tip(20, "hi"), 'Rating not recognised')
test.assert_equals(calculate_tip(107.65, "GReat"), 17)
test.assert_equals(calculate_tip(20, "great!"), 'Rating not recognised')
