list1 = [1,2,4,5,3,7,9]
list2 = [2,9,4,10,13]

commonElem = []
for i in list1 :
    if i in list2:
        commonElem.append(i)

print(commonElem)