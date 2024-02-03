list1 = [1,2,3,4,5,6,7,8,9,10]
maxVal = list1[0]

for i in list1:
    maxVal = max(maxVal,i)

print(f"Maximum value in {list1} is {maxVal}")