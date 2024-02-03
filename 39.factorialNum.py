list1 = []

def fact(num:int):
    fact = 1
    for i in range(1,num+1):
        fact *= i
    return fact

for i in range(1,11):
    list1.append(fact(i))

print(list1)