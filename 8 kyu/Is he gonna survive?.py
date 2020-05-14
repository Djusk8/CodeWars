# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/59ca8246d751df55cc00014c

8 kyu - Is he gonna survive?

A hero is on his way to the castle to complete his mission. However, he's been told that the castle is surrounded with a couple of powerful dragons! each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry.. Assuming he's gonna grab a specific given number of bullets and move forward to fight another specific given number of dragons, will he survive?
Return True if yes, False otherwise :)
"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def hero(bullets, dragons):
    return dragons * 2 <= bullets

# ---------------  TEST CASES ---------------
test.assert_equals(hero(10, 5), True)
test.assert_equals(hero(7, 4), False)
test.assert_equals(hero(4, 5), False)
test.assert_equals(hero(100, 40), True)
test.assert_equals(hero(1500, 751), False)
test.assert_equals(hero(0, 1), False)
