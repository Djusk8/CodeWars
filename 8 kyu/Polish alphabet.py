# ------------  KATA DESCRIPTION ------------
"""
8 kyu - Polish alphabet

There are 32 letters in the Polish alphabet: 9 vowels and 23 consonants. 
Your task is to change the letters with diacritics:
ą -> a,
ć -> c,
ę -> e,
ł -> l,
ń -> n,
ó -> o,
ś -> s,
ź -> z,
ż -> z

and print out the string without the use of the Polish letters.
For example:
"Jędrzej Błądziński"  -->  "Jedrzej Bladzinski"""

# ---------------  SOLUTION ---------------
import codewars_test as test


def correct_polish_letters(st):
    return st.translate(str.maketrans("ąćęłńóśźż", "acelnoszz"))


# ---------------  TEST CASES ---------------
@test.describe('Example Tests')
def example_tests():
    test.assert_equals(correct_polish_letters("Jędrzej Błądziński"),"Jedrzej Bladzinski");
    test.assert_equals(correct_polish_letters("Lech Wałęsa"),"Lech Walesa");
    test.assert_equals(correct_polish_letters("Maria Skłodowska-Curie"),"Maria Sklodowska-Curie")
