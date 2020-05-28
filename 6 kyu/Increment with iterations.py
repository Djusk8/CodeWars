# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/5ecc16daa200d2000165c5b1

6 kyu - Increment with iterations

Your goal in this kata is to implement an algorithm, which increases number in the way explained below, and returns the
result.
Input data: number, iterations, step.
Stage 1:
We get the: number:143726, iterations:  16, step:3
And make increment operations in a special way
Position: We start from 1 position and increment 4th num, besause step is 3
s - start position
+ - current increased position
Position: s - - - - - => - - - + - -
Number: 1 4 3 7 2 6 => 1 4 3 8 2 6
Stage 2: repeat stage 1 :)
Position: - - - s - - => + - - - - -
Number: 1 4 3 8 2 6 => 2 4 3 8 2 6
You must remember: if your number overflow into a longer number, the current position gets shifted to the right
9 9 9 => - - p - before overflow position be at 3rd digit
1 0 0 0 => - - - p - after overflow position be at 4th digit
Note:
9 => 10
799 => 800 (if you increase second 9) or 809 (if you increase first 9)
99000 => 100000 (if you increase second 9) or 109000 (if you increase first 9)

"""


# ---------------  SOLUTION ---------------
import codewars_test as test
from math import floor, log10


def increment(number, iterations, spacer):
    next_pos = 0
    for _ in range(iterations):
        num_ln = floor(log10(number) + 1)
        next_pos = (next_pos + spacer) % num_ln
        number += 10 ** (num_ln - next_pos - 1)
        if floor(log10(number) + 1) > num_ln:
            next_pos += 1
    return number


# ---------------  TEST CASES ---------------
@test.describe("Increment with iterations")
def test_increment():
    @test.it("given number:123, iterations:5, step: 2")
    def test1():
        test.assert_equals(increment(123,5,2), 245)

    @test.it("given number:14123, iterations:15, step: 6")
    def test2():
        test.assert_equals(increment(14123,15,6), 47456)
    
    @test.it("given number:9999, iterations:9, step: 9")
    def test3():
        test.assert_equals(increment(9999,9,9), 32211)
  
