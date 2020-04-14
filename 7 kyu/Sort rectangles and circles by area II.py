# ------------  KATA DESCRIPTION ------------
"""
7 kyu
Sort rectangles and circles by area II

In this kata you will be given a sequence of the dimensions of rectangles ( sequence with width and length ) and circles ( radius - just a number ).
Your task is to return a new sequence of dimensions, sorted ascending by area.

For example,

seq = [ (4.23, 6.43), 1.23, 3.444, (1.342, 3.212) ] # [ rectangle, circle, circle, rectangle ]
sort_by_area(seq) => [ ( 1.342, 3.212 ), 1.23, ( 4.23, 6.43 ), 3.444 ]
"""

# ---------------  SOLUTION ---------------
import codewars_test as test


def sort_by_area(seq):
    import math
    square = [elem[0]*elem[1] if type(elem) is tuple else elem**2 * math.pi for elem in seq ]
    result = dict(zip(square, seq))
    return [result[key] for key in sorted(result)]


# ---------------  TEST CASES ---------------
@test.describe('Example Tests')
def example_tests():
    test.assert_equals(sort_by_area([ (4.23, 6.43), 1.23, 3.444, (1.342, 3.212) ]), [ (1.342, 3.212), 1.23, (4.23, 6.43), 3.444 ] )
    test.assert_equals(sort_by_area([ (2, 5), 6 ]), [ (2, 5), 6 ])
    test.assert_equals(sort_by_area([]), [] )