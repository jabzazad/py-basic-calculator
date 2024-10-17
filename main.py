import calculator

listOfValues = []
isFinished = False
while not isFinished:
    mylist = calculator.inputs()
    value = 0
    if mylist[1] == "+":
       value= calculator.add(mylist[0], mylist[2])
    elif mylist[1] == "-":
        value= calculator.subtract(mylist[0], mylist[2])
    elif mylist[1] == "*":
       value = calculator.multiply(x, y)
    elif mylist[1] == "/":
       value=calculator.divide(mylist[0], mylist[2])

    print("The result is: ", value)
    listOfValues.append(value)
    print("result from list: ", sum(listOfValues))
    if input("Do you want to continue? (y/n): ") == "n":
        isFinished = True
        
