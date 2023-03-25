def myFun(x,y):
    return x+y

myFun.__subject__ = "bio"
myFun.__mark__ = 90
print(myFun.__subject__)
print(myFun.__mark__)

print(dir(myFun))