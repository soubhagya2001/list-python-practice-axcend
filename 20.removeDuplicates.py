list1 = [1,2,3,4,5,6,4,2,1]
print(f"Before removing duplicates : {list1}")

uniqueList = []
for i in list1:
    if i not in uniqueList:
        uniqueList.append(i)

print(f"After removing duplicates : {uniqueList}")