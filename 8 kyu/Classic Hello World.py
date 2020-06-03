# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/57036f007fd72e3b77000023

8 kyu - Classic Hello World

The main mode is having a method named main inside a class and should return nothing but should print a line to the
standard output with the message Hello World! i.e. print the line Hello World! to the console.
For Java the main method should receive String array as parameters that can be specified when running from console with
the command.
In many traditional programming languages can be only one main for a whole application since it denotes the application
entry point.

    Solution.main("parameter1", "parameter2","parametern")

    *Note:* please be sure to define main as static method

Hints:

Check your references
Think about the scope of your method
For prolog you can use write but there are better ways


"""


# ---------------  SOLUTION ---------------
import codewars_test as test


class Solution:
    @staticmethod
    def main(*args):
        print("Hello World!")

# ---------------  TEST CASES ---------------
test.describe("Basic tests")
#the preloaded testing functions calls the function and compares what
#it prints with the result parameter
test.it("Testing with no extra parameter")
test_solution_main(Solution.main, result="Hello World!")
test.it("Testing with 'Hola mundo!' as extra parameter")
test_solution_main(Solution.main,["Hola mundo!"],result="Hello World!")
