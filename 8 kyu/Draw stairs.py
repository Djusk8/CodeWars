# ------------  KATA DESCRIPTION ------------
"""
8 kyu - Draw stairs

given a number n, draw stairs with 'I' n tall and n wide, with the tallest in the top left.
Example (with - to represent spaces; DO NOT USE THEM IN THE SOLUTIONS! USE SPACES IN SOLUTION!
the "-"s are for clarity.): draw_stairs(3) == '''I\n_I\n__I'''

For example, a 7-step stairs should be drawn like this:

const sevenStepStairs = drawStairs(7);

I
 I
  I
   I
    I
     I
      I
"""


# ---------------  SOLUTION ---------------
def draw_stairs(n):
    return "\n".join([" "*i + "I" for i in range(n)])


# ---------------  TEST CASES ---------------
import codewars_test as test

stairs = '''I\n I\n  I'''
test.assert_equals(draw_stairs(3), stairs)