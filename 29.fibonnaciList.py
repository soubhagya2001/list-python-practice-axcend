list1 = [0,1]
for i in range(2,10):
    list1.append(list1[i-1] + list1[i-2])

print(list1)