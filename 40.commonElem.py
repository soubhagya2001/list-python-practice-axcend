list1 = [1,2,3,4,5,6]
list2 = [23,45,1,56,3]

noOfCommonElem = 0
for i in list1:
    if i in list2:
        noOfCommonElem +=1

print(f"Number of Common Elements in {list1} and {list2} is {noOfCommonElem}")