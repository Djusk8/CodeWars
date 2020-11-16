# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/5b5e0c0d83d64866bc00001d

7 kyu - Say Me Please Operations

You have a string with N numbers, starting with the third number each number is the result of an operation performed
using the previous two numbers.
Write a function which returns a string of the operations in order and separated by a comma and a space (e.g.
"subtraction, subtraction, addition").
Available operations are:

1) addition
2) subtraction
3) multiplication
4) division

Example: for string "9 4 5 20 25"
Your function must return:
"subtraction, multiplication, addition"
Because:

9 - 4 = 5 - substraction,
4 * 5 = 20 - multiplication,
5 + 20 = 25 - addition.


All input data is valid.
Number of numbers in input string >= 3.
For a case like "2 2 4" - when multiple variants are possible - choose the first possible operation from the list.
Integer division should be used.


"""


# ---------------  SOLUTION ---------------
import codewars_test as test

operations_list = {
    lambda x, y: x+y: "addition",
    lambda x, y: x-y: "subtraction",
    lambda x, y: x*y: "multiplication",
    lambda x, y: x//y: "division",
}


def sayMeOperations(stringNumbers):
    nums = list(map(int, stringNumbers.split()))
    result = list()

    for i in range(len(nums)-2):
        a, b, c = nums[i:i+3]
        for func in operations_list.keys():
            if func(a, b) == c:
                result.append(operations_list[func])
                break
    return ', '.join(result)


# ---------------  TEST CASES ---------------
@test.describe("say me operations")
def test_group():
    @test.it("basic")
    def basic():
        # test.assert_equals(sayMeOperations("1 2 3 5 8"), "addition, addition, addition")
        # test.assert_equals(sayMeOperations("9 4 5 20 25"), "subtraction, multiplication, addition")
        # test.assert_equals(sayMeOperations("10 2 5 -3 -15 12"), "division, subtraction, multiplication, subtraction")
        # test.assert_equals(sayMeOperations("2 2 4"), "addition")
        test.assert_equals(sayMeOperations("8 12 96 0 0"), "addition")
