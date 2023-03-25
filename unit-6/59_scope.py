#Scope of variables
#Global scope, local scope
#UnboundLocalError
g = 10

def myFun(n):
    global g #This changes g from local to global
    g = 20
    return g ** n

print(myFun(2))
print("global var g:::", g)

print("**********************************************")


#############################################################

#NonLocal


def outerFun():
    p = "green"
    def innerFun1():
        def innerFun2():
            print("innerMost p:",p)
        innerFun2()
        nonlocal p
        p = "python"
        print("innerFun1 p: ",p)
    innerFun1()
    print("outerFun p:",p)
    
outerFun()