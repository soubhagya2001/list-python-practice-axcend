list1 = [1,2,3,4,5,6,7,8,9,10]
minVal = list1[0]

for i in list1:
    minVal = min(minVal,i)

print(f"Minimum value in {list1} is {minVal}")