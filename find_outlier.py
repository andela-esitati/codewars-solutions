def find_outlier(integers):
    # create a list (list1) having the first four elements of integers
    # create another list (list2) only having the even numbers in list 1
    # if the length of list 2 is greater than one then it means the odd one out is an odd number
    # you should therefore return the odd on. out in integers
    # if the length of list 2 is not greater than one then it means most items are odd numbers
    # therefore return the even number
    list1 = integers[:4]
    list2 = [item for item in list1 if item % 2 == 0]
    if len(list2) > 1:
        list3 = [item for item in integers if item % 2 != 0]
        return list3[0]
    else:
        list4 = [item for item in integers if item % 2 == 0]
        return list4[0]
