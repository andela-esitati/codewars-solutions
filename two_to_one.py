def longest(s1, s2):
    # your code
    # join the two strings then convert them to a list
    # remove the duplicates
    # sort the remaining list without duplicates
    # join elements of the list to form a string
    list1 = sorted(set(list(s1 + s2)))
    return ''.join(list1)
