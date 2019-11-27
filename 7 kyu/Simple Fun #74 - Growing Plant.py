# ------------  KATA DESCRIPTION ------------
"""
7 kyu - Simple Fun #74: Growing Plant

Task

Each day a plant is growing by upSpeed meters. Each night that plant's height decreases by downSpeed meters due to the lack of sun heat. Initially, plant is 0 meters tall. We plant the seed at the beginning of a day. We want to know when the height of the plant will reach a certain level.
Example

For upSpeed = 100, downSpeed = 10 and desiredHeight = 910, the output should be 10.

 After day 1 --> 100
 After night 1 --> 90
 After day 2 --> 190
 After night 2 --> 180
 After day 3 --> 280
 After night 3 --> 270
 After day 4 --> 370
 After night 4 --> 360
 After day 5 --> 460
 After night 5 --> 450
 After day 6 --> 550
 After night 6 --> 540
 After day 7 --> 640
 After night 7 --> 630
 After day 8 --> 730
 After night 8 --> 720
 After day 9 --> 820
 After night 9 --> 810
 After day 10 --> 910

For upSpeed = 10, downSpeed = 9 and desiredHeight = 4, the output should be 1.

Because the plant reach to the desired height at day 1(10 meters).

 After day 1 --> 10

Input/Output

    [input] integer upSpeed

    A positive integer representing the daily growth.

    Constraints: 5 ≤ upSpeed ≤ 100.

    [input] integer downSpeed

    A positive integer representing the nightly decline.

    Constraints: 2 ≤ downSpeed < upSpeed.

    [input] integer desiredHeight

    A positive integer representing the threshold.

    Constraints: 4 ≤ desiredHeight ≤ 1000.

    [output] an integer

    The number of days that it will take for the plant to reach/pass desiredHeight (including the last day in the total count).


"""

# ---------------  SOLUTION ---------------
import codewars_test as Test


# Yes, it's not usual approach to solve this problem - mot times you will use day and height variables to store the data
# about the plant. I tried to find the way to make little optimization and remove the height variable.
def growing_plant(upSpeed, downSpeed, desiredHeight):
    day = 1

    while True:
        desiredHeight -= upSpeed
        if desiredHeight <= 0:
            return day
        else:
            day += 1
            desiredHeight += downSpeed


# ---------------  TEST CASES ---------------
Test.describe("Basic Tests")
Test.assert_equals(growing_plant(100,10,910),10)
Test.assert_equals(growing_plant(10,9,4),1)
Test.assert_equals(growing_plant(5,2,0),1)
Test.assert_equals(growing_plant(5,2,5),1)
Test.assert_equals(growing_plant(5,2,6),2)