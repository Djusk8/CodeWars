# ------------  KATA DESCRIPTION ------------
"""
6 kyu
Give me a Diamond

Jamie is a programmer, and James' girlfriend. She likes diamonds, and wants a diamond string from James. Since James doesn't know how to make this happen, he needs your help.
Task

You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*) characters. Trailing spaces should be removed, and every line must be terminated with a newline character (\n).

Return null/nil/None/... if the input is an even number or negative, as it is not possible to print a diamond of even or negative size.
Examples

A size 3 diamond:

 *
***
 *

...which would appear as a string of " *\n***\n *\n"

A size 5 diamond:

  *
 ***
*****
 ***
  *

...that is: " *\n ***\n*****\n ***\n *\n"

"""

# ---------------  SOLUTION ---------------
import codewars_test as test


def diamond(n):
    if n < 0 or n % 2 == 0:
        return None

    mas = []

    for i in range(1, n + 1, 2):
        mas.append(" " * ((n - i) // 2) + "*" * i + "\n")

    for j in range(len(mas) - 1, 0, -1):
        mas.append(mas[j - 1])

    return "".join(mas)


# ---------------  TEST CASES ---------------
expected =  " *\n"
expected += "***\n"
expected += " *\n"
test.assert_equals(diamond(1), "*\n")
test.assert_equals(diamond(2), None)
test.assert_equals(diamond(3), expected)
test.assert_equals(diamond(5), "  *\n ***\n*****\n ***\n  *\n")
test.assert_equals(diamond(0), None)
test.assert_equals(diamond(-3), None)