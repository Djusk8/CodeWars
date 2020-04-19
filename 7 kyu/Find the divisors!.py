# ------------  KATA DESCRIPTION ------------
"""
7 kyu
Find the divisors!

Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's
divisors(except for 1 and the number itself), from smallest to largest.
If the number is prime return the string '(integer) is prime' (null in C#)
(use Either String a in Haskell and Result<Vec<u32>, String> in Rust).
Example:

divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"
"""

# ---------------  SOLUTION ---------------
import codewars_test as Test


def divisors(integer):
    result = [num for num in range(2, integer) if not integer % num]
    return result if result else f"{integer} is prime"


# ---------------  TEST CASES ---------------
Test.assert_equals(divisors(15), [3, 5]);
Test.assert_equals(divisors(12), [2, 3, 4, 6]);
Test.assert_equals(divisors(13), "13 is prime");