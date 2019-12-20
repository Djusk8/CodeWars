# ------------  KATA DESCRIPTION ------------
"""
6 kyu - The Deaf Rats of Hamelin

Story

The Pied Piper has been enlisted to play his magical tune and coax all the rats out of town.

But some of the rats are deaf and are going the wrong way!
Kata Task

How many deaf rats are there?
Legend

    P = The Pied Piper
    O~ = Rat going left
    ~O = Rat going right

Example

    ex1 ~O~O~O~O P has 0 deaf rats

    ex2 P O~ O~ ~O O~ has 1 deaf rat

    ex3 ~O~O~O~OP~O~OO~ has 2 deaf rats

"""

# ---------------  SOLUTION ---------------
import codewars_test as Test
import re


def count_deaf_rats(town):
    town = town.replace(" ", "").split("P")

    l = re.findall(r'..', town[0])
    r = re.findall(r'..', town[1])

    return l.count("O~") + r.count("~O")


# ---------------  TEST CASES ---------------
Test.it("ex1")
Test.assert_equals(count_deaf_rats("~O~O~O~O P"), 0)

Test.it("ex2")
Test.assert_equals(count_deaf_rats("P O~ O~ ~O O~"), 1)

Test.it("ex3")
Test.assert_equals(count_deaf_rats("~O~O~O~OP~O~OO~"), 2)