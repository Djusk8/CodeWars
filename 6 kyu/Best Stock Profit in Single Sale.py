# ------------  KATA DESCRIPTION ------------
"""
6 kyu
Best Stock Profit in Single Sale

You're a buyer/seller and your buisness is at stake... You need to make profit... Or at least, you need to lose the
least amount of money! Knowing a list of prices for buy/sell operations, you need to pick two of them.
Buy/sell market is evolving across time and the list represent this evolution. First, you need to buy one item,
then sell it later. Find the best profit you can do.

Example:

Given an array of prices [3, 10, 8, 4], the best profit you could make would be 7 because you buy at 3 first, then sell at 10.
Input:

A list of prices (integers), of length 2 or more.
Output:

The result of the best buy/sell operation, as an integer.

Note:

Be aware you'll face lists with several thousands of elements, so think about performance.

"""

# ---------------  SOLUTION ---------------
import codewars_test as Test


def max_profit(prices):
    if prices.index(min(prices)) < prices.index(max(prices)):
        return max(prices) - min(prices)
    elif prices.index(min(prices)) == prices.index(max(prices)):
        if len(prices) == 1:
            return -prices[0]
        return 0
    else:
        try:
            profit_1 = max(prices) - min(prices[:prices.index(max(prices))])
        except ValueError:
            profit_1 = float('-inf')
        profit_2 = max_profit(prices[prices.index(max(prices))+1:])
        return max(profit_1, profit_2)


# ---------------  TEST CASES ---------------
@Test.describe("Fixed tests")
def _():
    Test.assert_equals(max_profit([49,50,30,40,2,5]), 10)
    Test.assert_equals(max_profit([10, 7, 5, 8, 11, 9]), 6)
    Test.assert_equals(max_profit([3, 4]), 1)
    Test.assert_equals(max_profit([9,9]), 0)
    Test.assert_equals(max_profit([10, 7, 5, 4, 1]), -1)