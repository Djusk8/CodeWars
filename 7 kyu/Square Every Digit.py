import codewars_test as Test


def square_digits(num):

    result = [str(num**2) for num in map(int, str(num))]

    return int(''.join(result))


Test.assert_equals(square_digits(9119), 811181)