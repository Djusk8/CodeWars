# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/55cbd4ba903825f7970000f5

8 kyu - Grasshopper - Grade book

Grade book
Complete the function so that it finds the mean of the three scores passed to it and returns the letter value associated
with that grade.

Numerical Score
Letter Grade

90 <= score <= 100
'A'

80 <= score < 90
'B'

70 <= score < 80
'C'

60 <= score < 70
'D'

0 <= score < 60
'F'

Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.
"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def get_grade(s1, s2, s3):
    score = (s1 + s2 + s3) / 3

    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    elif 0 <= score < 60:
        return 'F'


# ---------------  TEST CASES ---------------
test.describe("grade book")
test.it("should return an A")
test.assert_equals(get_grade(95, 90, 93), "A", "get_grade(95, 90, 93)")
test.assert_equals(get_grade(100, 85, 96), "A", "get_grade(100, 85, 96)")
test.assert_equals(get_grade(92, 93, 94), "A", "get_grade(92, 93, 94)")

test.it("should return a B")
test.assert_equals(get_grade(70, 70, 100), "B", "get_grade(70, 70, 100)")
test.assert_equals(get_grade(82, 85, 87), "B", "get_grade(82, 85, 87)")
test.assert_equals(get_grade(84, 79, 85), "B", "get_grade(84, 79, 85)")

test.it("should return a C")
test.assert_equals(get_grade(70, 70, 70), "C", "get_grade(70, 70, 70)")
test.assert_equals(get_grade(75, 70, 79), "C", "get_grade(75, 70, 79)")
test.assert_equals(get_grade(60, 82, 76), "C", "get_grade(60, 82, 76)")

test.it("should return a D")
test.assert_equals(get_grade(65, 70, 59), "D", "get_grade(65, 70, 59)")
