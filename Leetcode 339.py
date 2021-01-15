def helper(List, count):
    temp = 0
    for L in List:
        if L.isInteger():
            temp += L.getInteger() * count
        else:
            temp += helper(L.getList(), count+1)
    return temp

return helper(nestedList, 1)
