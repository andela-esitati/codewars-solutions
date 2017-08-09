def add(*args):
    # your code here
    # loop through the list of indexes and values tuples
    # add one to the index and multiply it with the value at the index
    # find the summation for the list



    return sum([(index + 1) * arg for index, arg in enumerate(args)])
