# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/58dced7b702b805b200000be

8 kyu - Geometry Basics: Distance between points in 2D

This series of katas will introduce you to basics of doing geometry with computers.
Point objects have x and y attributes (X and Y in C#) attributes.
Write a function calculating distance between Point a and Point b.
Tests round answers to 6 decimal places.

"""


# ---------------  SOLUTION ---------------
def distance_between_points(a, b):
    return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5


# ---------------  TEST CASES ---------------
import codewars_test as test
from solution import distance_between_points
from preloaded import Point


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(distance_between_points(Point(3, 3), Point(3, 3)), 0)
        test.assert_equals(distance_between_points(Point(1, 6), Point(4, 2)), 5)
        test.assert_equals(round(distance_between_points(Point(-10.2, 12.5), Point(0.3, 14.7)), 6), 10.728001)
