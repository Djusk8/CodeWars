# ------------  KATA DESCRIPTION ------------
"""
https://www.codewars.com/kata/568dc014440f03b13900001d

8 kyu - L1: Bartender, drinks!

Write a function getDrinkByProfession/get_drink_by_profession() that receives as input parameter a string, and produces
outputs according to the following table:



Input
Output

"Jabroni"
"Patron Tequila"

"School Counselor"
"Anything with Alcohol"

 "Programmer"
 "Hipster Craft Beer"

 "Bike Gang Member"
"Moonshine" 

 "Politician"
"Your tax dollars" 

 "Rapper"
"Cristal" 

 *anything else*
"Beer" 


Note: anything else is the default case: if the input to the function is not any of the values in the table, then the
return value should be "Beer."
Make sure you cover the cases where certain words do not show up with correct capitalization. For example,
getDrinkByProfession("pOLitiCIaN") should still return "Your tax dollars".
"""


# ---------------  SOLUTION ---------------
import codewars_test as test


def get_drink_by_profession(param):
    drinks = {
        "jabroni": "Patron Tequila",
        "school counselor": "Anything with Alcohol",
        "programmer": "Hipster Craft Beer",
        "bike gang member": "Moonshine",
        "politician": "Your tax dollars",
        "rapper": "Cristal"
    }

    return drinks[param.lower()] if param.lower() in drinks.keys() else "Beer"


# ---------------  TEST CASES ---------------
test.assert_equals(get_drink_by_profession("jabrOni"), "Patron Tequila", "'Jabroni' should map to 'Patron Tequila'")
test.assert_equals(get_drink_by_profession("scHOOl counselor"), "Anything with Alcohol", "'School Counselor' should map to 'Anything with alcohol'")
test.assert_equals(get_drink_by_profession("prOgramMer"), "Hipster Craft Beer", "'Programmer' should map to 'Hipster Craft Beer'")
test.assert_equals(get_drink_by_profession("bike ganG member"), "Moonshine", "'Bike Gang Member' should map to 'Moonshine'")
test.assert_equals(get_drink_by_profession("poLiTiCian"), "Your tax dollars", "'Politician' should map to 'Your tax dollars'")
test.assert_equals(get_drink_by_profession("rapper"), "Cristal", "'Rapper' should map to 'Cristal'")
test.assert_equals(get_drink_by_profession("pundit"), "Beer", "'Pundit' should map to 'Beer'")
test.assert_equals(get_drink_by_profession("Pug"), "Beer", "'Pug' should map to 'Beer'")
