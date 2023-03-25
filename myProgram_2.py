list1 = [1,2,3,4,5,6,7,8,9]
list2 = ["*","$"]

def numFun(list1):
    for i in list1:
        print(i,end="  ")
    print(" ")

def secFun(list1,list2):
    print(list1[0],end="  ")
    for i in range(7):
        print(list2[0],end="  ")
    print("9")
    
def tirFun(list1,list2):
    print(list1[0],end="  ")
    for i in range(2):
        print(list2[0], end="  ")
    for i in range(3):
        print(list2[1],end="  ")
    for i in range(2):
        print(list2[0],end="  ")
    print(list1[-1])

numFun(list1)
for i in range(2):
    secFun(list1,list2)

for i in range(3):
    tirFun(list1,list2)
    
for i in range(2):
    secFun(list1,list2)
numFun(list1)

