# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/57e921d8b36340f1fd000059

8 kyu - Holiday VI - Shark Pontoon

Your friend invites you out to a cool floating pontoon around 1km off the beach. Among other things, the pontoon has a
huge slide that drops you out right into the ocean, a small way from a set of stairs used to climb out.
As you plunge out of the slide into the water, you see a shark hovering in the darkness under the pontoon... Crap!
You need to work out if the shark will get to you before you can get to the pontoon. To make it easier... as you do the
mental calculations in the water you either freeze when you realise you are dead, or swim when you realise you can make
it!
You are given 5 variables:
sharkDistance = distance the shark needs to cover to eat you in metres,
sharkSpeed = how fast it can move in metres/second,
pontoonDistance = how far you need to swim to safety in metres,
youSpeed = how fast you can swim in metres/second,
dolphin = a boolean, if true, you can half the swimming speed of the shark as the dolphin will attack it.
If you make it, return "Alive!", if not, return "Shark Bait!".
"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    return "Alive!" if pontoon_distance / you_speed < shark_distance / shark_speed * (2 if dolphin else 1) else "Shark Bait!"


# ---------------  TEST CASES ---------------
test.assert_equals(shark(12, 50, 4, 8, True), "Alive!");
test.assert_equals(shark(7, 55, 4, 16, True), "Alive!");
test.assert_equals(shark(24, 0, 4, 8, True), "Shark Bait!");
test.assert_equals(shark(37, 92, 2, 13, False), "Shark Bait!");
