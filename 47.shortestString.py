listOfString = ["hi, how are you?","I am fine","What about you?","I am also fine"]

minStringLength = len(listOfString[0])
stringi = ""
for i in listOfString:
    stringLength = len(i)
    
    if stringLength < minStringLength:
        minStringLength = stringLength
        stringi = i

print(f"Min length string in the list is '{stringi}' of length {minStringLength}")