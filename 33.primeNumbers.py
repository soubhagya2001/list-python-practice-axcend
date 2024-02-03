def isPrime(num:int):
    if num==1 or num==0:
        return False
    
    for i in range(2,num):
       if i == num:
           break
       if num%i == 0:
           return False
       
    return True
       
list1 = []
for i in range(51):
    if isPrime(i):
        list1.append(i)  

print(list1)