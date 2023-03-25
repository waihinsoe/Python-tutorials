print(callable(print))
print(callable('xyz'.upper))
text = print("hello")
print(text)

ls = [1,2,3,4]
test = ls.append(5)
print(ls)
print(test)

#print len callable
# str.upper list.append
#def lambda : expression
#All object are not callable

from decimal import Decimal
print(callable(Decimal))

a = Decimal('10.10')
print(type(a))
print(callable(a))
print("##################################################################")

#######example 
class myClass:
    def __init__(self, x=0):
        print("from class")
        self.counter = x
        
    def __call__(self , x=1):
        print("updating value.....")
        self.counter += x
        
    def myFun(self , z=1):
        print("from myFun new.....")
        self.counter +=z

inObj = myClass()       
myObj = myClass()
myFunObj = myClass()

print(myClass.__init__(inObj , 20))
print("################")
print(myClass.__call__(myObj,10))
print("################")
print(myClass.myFun(myFunObj,30))
print("################")

print(inObj.counter)
print(callable(inObj))

print(myObj.counter)
print(callable(myObj))
        
inObj()
print(inObj.counter)

myObj()
print(myObj.counter)

print("myfunobj value is ",myFunObj.counter)

myFunObj()
print("after updating")
print(myFunObj.counter)