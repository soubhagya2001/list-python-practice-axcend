list1 = [[1,2,3],[4,5,6],[7,8,9]]
list2 = []

for i in list1:
    for j in i:
        list2.append(j)

print(list2)