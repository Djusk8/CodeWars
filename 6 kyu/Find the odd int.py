import codewars_test as test


def find_it(seq):
    for item in set(seq):
        if seq.count(item) % 2 == 1:
            return item


test.describe("Example")
test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)

