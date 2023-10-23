def item_in_common(list1, list2):
    myDict = { }

    for i in list1: 
        myDict[i] = True

    for j in list2: 
        if j in myDict: 
            return True
    return False

list1 = [1,3,5]
list2 = [2,4,6]

print(item_in_common(list1, list2))

