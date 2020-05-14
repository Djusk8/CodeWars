# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/5635e7cb49adc7b54500001c

7 kyu - ATM

There is enough money available on ATM in nominal value 10, 20, 50, 100, 200 and 500 dollars.
You are given money in nominal value of n with 1<=n<=1500.
Try to find minimal number of notes that must be used to repay in dollars, or output -1 if it is impossible.
Good Luck!!!
"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def solve(n):
    if n % 10:
        return -1
    else:
        x = n // 500
        n = n % 500
        x += n // 200
        n = n % 200
        x += n // 100
        n = n % 100
        x += n // 50
        n = n % 50
        x += n // 20
        n = n % 20
        x += n // 10
        return x

# ---------------  TEST CASES ---------------
test.describe("solve")

test.it("should work when chosing notes is possible")
test.assert_equals(solve(770), 4, "Wrong result for 770")
test.assert_equals(solve(550), 2, "Wrong result for 550")
test.assert_equals(solve(10), 1, "Wrong result for 10")
test.assert_equals(solve(1250), 4, "Wrong result for 1250")
test.assert_equals(solve(1500), 3,  "Wrong result for 1500")

  
test.it("should return -1 if chosing notes is not possible")
test.assert_equals(solve(125), -1, "Wrong result for 125")
test.assert_equals(solve(666), -1, "Wrong result for 666")
test.assert_equals(solve(42), -1, "Wrong result for 42")

