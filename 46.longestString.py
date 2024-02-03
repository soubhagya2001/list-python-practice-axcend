listOfString = ["hi, how are you?","I am fine","What about you?","I am also fine"]

maxStringLength = 0
stringi = ""
for i in listOfString:
    stringLength = len(i)
    
    if stringLength > maxStringLength:
        maxStringLength = stringLength
        stringi = i

print(f"Max length string in the list is '{stringi}' of length {maxStringLength}")