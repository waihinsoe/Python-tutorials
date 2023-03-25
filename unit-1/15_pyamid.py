row = int(input("Please enter row "))
size = row 
cow = size
for i in range(1,row):
    for a in range(size):
        print(end=" ")
    size -= 1

    for c in range(1,(i*2)):
        print("*",end="")

    for d in range(cow):
        print(end=" ")
    cow -= 1
    print(" ")