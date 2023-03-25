#Closure Attribute
#__closure__
#__closure__.cell_contents
def myFun(n):
    def adding(data):
        return data+n
    return adding

add10 = myFun(10)
print("add10 :" ,add10(20))
print(add10.__closure__)
print(add10.__closure__[0].cell_contents)

def myFun1(x,y):
    return x+y

print(myFun1.__closure__)
