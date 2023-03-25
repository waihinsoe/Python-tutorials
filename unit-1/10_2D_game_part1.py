import secrets 
import sys
secureNumber = secrets.SystemRandom()

while True:
    print("___Welcome to our Game___")
    press1 = int(input("Press1 for read rule and press2 for play game :>"))
    if press1 == 1:
        print("Age must be more than 18 :")
        print("Show money more than 5000")
        print("U must be use more than 1000 each time :")
    if press1 == 2:
        uName = input("Please enter your name :>")
        uAge = int(input("Please enter your age :>"))

        while len(uName) > 2 and uAge > 17 :
            print("You can play game now ")
            print("Welcome :> ",uName)
            while True:
                sMoney = int(input("Please enter your money :>"))
             
                while sMoney > 4999:
                    while True:
                        print("Your show money are :>",sMoney)
                        inputMoney = int(input("Please enter your money to play :>"))
                        luckyNumber = int(input("Please enter lucky number :>"))
                        systemNumber = secureNumber.randint(10,99)
                    
                        if luckyNumber ==systemNumber:
                            print("You are win in 2D game")
                            sMoney = (inputMoney*10) + (sMoney - inputMoney)
                            print("This is your all money $ :>",sMoney)
                            toQuit = int(input("Press0 to start game again"))
                            if toQuit != 0:
                                sys.exit("bye bye")
                            else:
                                continue
                            
                        print("Try again......lucky number is :>",systemNumber)
                        sMoney = sMoney - inputMoney
                        if sMoney <1000:
                            print("You have not enough money $ :>",sMoney)
                            break
                print("Please fill again money more")

        print("Please read again game rule")

