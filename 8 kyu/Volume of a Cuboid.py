# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/58261acb22be6e2ed800003a

8 kyu - Volume of a Cuboid

Bob needs a fast way to calculate the volume of a cuboid with three values: length, width and the height of the cuboid.
Write a function to help Bob with this calculation.
"""


# ---------------  SOLUTION ---------------
import codewars_test as test


getVolumeOfCubiod = lambda a,b,c: a*b*c


# ---------------  TEST CASES ---------------
test.assert_equals(getVolumeOfCubiod(1, 2, 2), 4)
test.assert_equals(getVolumeOfCubiod(6.3, 2, 5), 63)
