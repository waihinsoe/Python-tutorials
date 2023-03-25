import secrets
import sys
secureNumber = secrets.SystemRandom()

while True:
    print("____Welcome to my game____")
    press1 = int(input("Press1 to read rule and press2 to play game :>"))
    if press1 == 1:
        print("Age must be 18")
        print("Show money more than 5000")
        print("U must use 1000 each time")

    if press1 == 2:
        uName = input("Please enter your name :>")
        uAge = int(input("Please enter your age :>"))

        while len(uName) > 2 and uAge > 17 :
            print("You can play game now")
            print("Welcome :>",uName)
            while True:
                sMoney = int(input("Please enter your show money :>"))
                while sMoney > 4999:
                    while True:
                        print("This is your  money $ :>",sMoney)
                        inputMoney = int(input("Please enter money to play :>"))
                        luckyNumber = input("Please enter your lucky Number :>")
                        systemNumber = secureNumber.randint(10,99)
                        if inputMoney >= 1000 and luckyNumber.isdigit() and len(luckyNumber) > 1 and len(luckyNumber) < 3:
                            if int(luckyNumber) == systemNumber:
                                print("You win in 2D game")
                                sMoney = (inputMoney*10) + (sMoney - inputMoney)
                                print("This is your all money $ :>",sMoney)
                                toQuit = int(input("Press0 to play again :>"))
                                if toQuit != 0:
                                    sys.exit("Bye Bye")
                                else:
                                    continue
                                
                            print("Try again________lucky Number is :>",systemNumber)
                            sMoney = sMoney - inputMoney
                            if sMoney == 0:
                                print("You don't have money! Please fill more :>",sMoney)
                                break
                        else: 
                            print("Try again somethings wrong check out")
                print("Show money need more")
        print("Please read more game rule")