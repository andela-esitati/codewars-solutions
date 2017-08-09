def swap(string_):
    # your code here
    # convert the string to a list of chracher elements
    # loop through the list and check for wether the elements are uppercase or lowercase
    # append the element changed to the right casing to another list
    # append numbers just the way they are
    # join the characters in the list to form a string

    list2 = list(string_)
    list3 = []
    for item in list2:
        if item.islower():
            list3.append(item.upper())
        elif item.isupper():
            list3.append(item.lower())
        else:
            list3.append(item)
    return ''.join(list3)
