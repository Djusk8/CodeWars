def find_outlier(integers):
    evens = [num % 2 for num in integers]

    if evens.count(0) == 1:  # if there is one even integer in the list
        return integers[evens.index(0)]
    else:
        return integers[evens.index(1)]