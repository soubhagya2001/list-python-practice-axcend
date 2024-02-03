power = int(input("Enter how much power you want : "))

list1 = []
for i in range(1,power+1):
    list1.append(2**i)

print(list1)