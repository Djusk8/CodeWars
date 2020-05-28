# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/582cb0224e56e068d800003c

8 kyu - Keep Hydrated!

Nathan loves cycling.
Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest
value.
For example:
time = 3 ----> litres = 1
time = 6.7---> litres = 3
time = 11.8--> litres = 5

"""


# ---------------  SOLUTION ---------------
import codewars_test as test

litres = lambda x: int(x*0.5)


# ---------------  TEST CASES ---------------
test.describe('Fixed tests')
test.it('Tests')
test.assert_equals(litres(2), 1, 'should return 1 litre');
test.assert_equals(litres(1.4), 0, 'should return 0 litres');
test.assert_equals(litres(12.3), 6, 'should return 6 litres');
test.assert_equals(litres(0.82), 0, 'should return 0 litres');
test.assert_equals(litres(11.8), 5, 'should return 5 litres');
test.assert_equals(litres(1787), 893, 'should return 893 litres');
test.assert_equals(litres(0), 0, 'should return 0 litres');
