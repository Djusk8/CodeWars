# ------------  KATA DESCRIPTION ------------
"""
7 kyu - The wheat/rice and chessboard problem

I assume most of you are familiar with the ancient legend of the rice (but I see wikipedia suggests wheat, for some reason) problem, but a quick recap for you: a young man asks as a compensation only 1 grain of rice for the first square, 2 grains for the second, 4 for the third, 8 for the fourth and so on, always doubling the previous.

Your task is pretty straightforward (but not necessarily easy): given an amount of grains, you need to return up to which square of the chessboard one should count in order to get at least as many.

As usual, a few examples might be way better than thousands of words from me:

squares_needed(0) == 0
squares_needed(1) == 1
squares_needed(2) == 2
squares_needed(3) == 2
squares_needed(4) == 3

Input is always going to be valid/reasonable: ie: a non negative number;
extra cookie for not using a loop to compute square-by-square (at least not directly) and instead trying a smarter
approach [hint: some peculiar operator]; a trick converting the number might also work: impress me!
"""

# ---------------  SOLUTION ---------------
import codewars_test as Test


def squares_needed(grains):
    return 0 if grains == 0 else len(bin(grains))-2


# ---------------  TEST CASES ---------------
Test.describe("Basic tests")
Test.assert_equals(squares_needed(0), 0)
Test.assert_equals(squares_needed(1), 1)
Test.assert_equals(squares_needed(2), 2)
Test.assert_equals(squares_needed(3), 2)
Test.assert_equals(squares_needed(4), 3)
print("<COMPLETEDIN::>")

Test.describe("Random tests")
from random import randint
sol=lambda n: 1+sol(n>>1) if n else n

for _ in range(40):
    n=randint(1,10**randint(1,15))
    Test.it("Testing for "+str(n))
    Test.assert_equals(squares_needed(n), sol(n), "It should work for random inputs too")