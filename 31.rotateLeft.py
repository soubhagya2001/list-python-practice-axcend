list1 = [1,2,3,4,5,6,7,8,9,10]

print(f"List before rotating : {list1}")
pos = int(input("Rotate left by : "))

for i in range(0,pos):
    list1.append(list1.pop(0))

print(f"List after rotating : {list1}")