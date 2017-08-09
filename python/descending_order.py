def Descending_Order(num):
    # Bust a move right here
    # convert num to a string
    # convert the formed string to a list
    # sort the list and arrange it in descending order
    # join the list to form a string
    # return the string converted to a number
    string = str(num)
    list1 = reversed(sorted(list(string)))
    string2 = ''.join(list1)
    return int(string2)
