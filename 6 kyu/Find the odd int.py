def find_it(seq):
    items = set(seq)
    for item in items:
        cnt = items.count(item)

    return None



import codewars_test as test

test.describe("Example")
test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)

