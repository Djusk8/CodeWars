# ------------  KATA DESCRIPTION ------------
"""

"""

# ---------------  SOLUTION ---------------
import codewars_test as Test


def fight(robot_1, robot_2, tactics):

    pass


# ---------------  TEST CASES ---------------
robot_1 = {"name": "Rocky", "health": 100, "speed": 20, "tactics": ["punch", "punch", "laser", "missile"] }
robot_2 = {"name": "Missile Bob", "health": 100, "speed": 21, "tactics": ["missile", "missile", "missile", "missile"]}
tactics = {"punch": 20, "laser": 30, "missile": 35}
Test.assert_equals(fight(robot_1, robot_2, tactics), "Missile Bob has won the fight.")

robot_1 = {"name": "Rocky", "health": 200, "speed": 20, "tactics": ["punch", "punch", "laser", "missile"] }
robot_2 = {"name": "Missile Bob", "health": 100, "speed": 21, "tactics": ["missile", "missile", "missile", "missile"]}
tactics = {"punch": 20, "laser": 30, "missile": 35}
Test.assert_equals(fight(robot_1, robot_2, tactics), "Rocky has won the fight.")