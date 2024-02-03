list1 = [-1,-2,5,7,-2,19]
print(f"Original list : {list1}")

for i in range(len(list1)):
    if list1[i]<0:
        list1[i] = 0

print(f"Modified list : {list1}")