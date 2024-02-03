list1 = [1,3,2,4,5,6]

isSorted = True
for i in range(1,len(list1)-1):
    if list1[i] > list1[i+1]:
        isSorted = False
    

print("Sorted") if isSorted else print('Not Sorted')