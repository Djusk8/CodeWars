# ------------  KATA DESCRIPTION ------------
"""
8 kyu - For UFC Fans (Total Beginners): Conor McGregor vs George Saint Pierre

This is a beginner friendly kata especially for UFC/MMA fans.

It's a fight between the two legends: Conor McGregor vs George Saint Pierre in Madison Square Garden. Only one fighter will remain standing, and after the fight in an interview with Joe Rogan the winner will make his legendary statement. It's your job to return the right statement depending on the winner!

If the winner is George Saint Pierre he will obviously say:

    "I am not impressed by your performance."

If the winner is Conor McGregor he will most undoubtedly say:

    "I'd like to take this chance to apologize.. To absolutely NOBODY!"

Good Luck!
"""


# ---------------  SOLUTION ---------------
def quote(fighter):
    if fighter.lower() == "george saint pierre":
        return "I am not impressed by your performance."
    else:
        return "I'd like to take this chance to apologize.. To absolutely NOBODY!"


# ---------------  TEST CASES ---------------
import codewars_test as Test

Test.assert_equals(quote('george saint pierre'), "I am not impressed by your performance.")
Test.assert_equals(quote('conor mcgregor'), "I'd like to take this chance to apologize.. To absolutely NOBODY!")

Test.assert_equals(quote('George Saint Pierre'), "I am not impressed by your performance.")
Test.assert_equals(quote('Conor McGregor'), "I'd like to take this chance to apologize.. To absolutely NOBODY!")
