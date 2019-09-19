import codewars_test as test


def duplicate_count(text):
    return sum([text.lower().count(item) > 1 for item in set(text.lower())])


test.assert_equals(duplicate_count(""), 0)
test.assert_equals(duplicate_count("abcde"), 0)
test.assert_equals(duplicate_count("abcdeaa"), 1)
test.assert_equals(duplicate_count("abcdeaB"), 2)
test.assert_equals(duplicate_count("Indivisibilities"), 2)

lowercase, uppercase = 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

test.assert_equals(duplicate_count(lowercase), 0)
test.assert_equals(duplicate_count(lowercase + "aaAb"), 2)

test.assert_equals(duplicate_count(lowercase+lowercase), 26)
test.assert_equals(duplicate_count(lowercase+uppercase), 26)