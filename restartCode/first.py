def welcome():
    print("Press 1 to register", end="\n")
    print("Press 2 to Login", end="\n")
    print("Press 3 to exit", end="\n")
    option = int(input("Enter option number=>"))
    if(option == 1):
        print("This is registration", end="\n")
        register()
    elif(option == 2):
        print("This is login", end="\n")
        # login()
    elif(option == 3):
        exit(1)
    else:
        print("wrong option", end="\n")
        welcome()

def register():
    email = input("Enter your email : ")
    name = input("Enter your name : ")
    password = input("Enter your password : ")

    print(email, name, password)


welcome()