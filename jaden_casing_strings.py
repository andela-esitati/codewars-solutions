def toJadenCase(string):
    # make a list of every single word in the list
    # capitalize every word in the list and append it to another list
    # return the elemens of that list joined to form a string
    list1 = string.split()
    list2 = []
    for item in list1:
        list2.append(item.capitalize())
    return ' '.join(list2)
