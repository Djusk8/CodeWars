# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/5630d1747935943168000013

7 kyu - Tally it up

I'm creating a scoreboard on my game website, but I want the score to be displayed as tally marks instead of Roman
numerals. Write a function that translates the numeric score into tally marks.
My tally mark font uses the letters a, b, c, d, e to represent tally marks for 1, 2, 3, 4, 5, respectively. I want a
space and line break (
) after each completed tally (5).
Assume that the score you receive will be an integer. This function should return an HTML string that I can insert into
my website that represents the correct score.

"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def score_to_tally(s):
    return "e <br>" * (s // 5) + {0: "", 1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e <br>'}[s % 5]


# ---------------  TEST CASES ---------------
import codewars_test as test
# from solution import score_to_tally

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(score_to_tally(3),'c', "Should return 'c'")
        test.assert_equals(score_to_tally(10),'e <br>e <br>', "Should return 'e <br>e <br>'")
        test.assert_equals(score_to_tally(5),'e <br>', "Should return 'e <br>'")
        test.assert_equals(score_to_tally(1),'a')
        test.assert_equals(score_to_tally(16),'e <br>e <br>e <br>a')
        test.assert_equals(score_to_tally(28),'e <br>e <br>e <br>e <br>e <br>c')
        test.assert_equals(score_to_tally(19),'e <br>e <br>e <br>d')
        test.assert_equals(score_to_tally(9),'e <br>d')
        test.assert_equals(score_to_tally(15),'e <br>e <br>e <br>')
        test.assert_equals(score_to_tally(7),'e <br>b')

