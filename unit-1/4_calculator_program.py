#Calculator 
print("Press 1 : For add")
print("Press 2 : For subtract")
print("Press 3 : For multiply")
print("Press 4 : For divide")

userInput = int(input("Please enter something :"))
firstNumber = int(input("Please enter firstNumber"))
secondNumber = int(input("Please enter secondNumber"))

if userInput == 1 :
    result = firstNumber + secondNumber
elif userInput == 2 :
    result = firstNumber - secondNumber
elif userInput == 3 :
    result = firstNumber * secondNumber
elif userInput == 4 :
    result = firstNumber / secondNumber
else:
    print("Please must enter 1/2/3/4")
print("The result of {} {} {} is {}".format(firstNumber,userInput,secondNumber,result))
