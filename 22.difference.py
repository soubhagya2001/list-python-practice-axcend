list1 = [1,2,4,5,3,7,9]
list2 = [2,9,4,10,13]

temp3 = []
for element in list1:
    if element not in list2:
        temp3.append(element)
 
print(temp3)