#Encapsulation 
 ##Public    => Use normal variable and method 
 ##Private   => __variable and method (double underscore)
 ##Protected => -variable and method (single underscore)

class Myclass:
    def __init__(self,age) -> None:
        self._age = age #don't touch from the outside
        
class Sub(Myclass): #Does derived class with method 
    def getData(self):
        print(self._age)

obj = Sub(100)
obj.getData()# use like this

#Don't use this
# obj._age = 20
#print(obj._age)