list1 = [1,2,3,4,5]

lengthOfList = len(list1)

for i in range(lengthOfList):
    num = list1.pop(0)
    list1.append(num*num)

print(list1)