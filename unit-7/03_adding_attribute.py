##### Adding attribute form outer to class
# class MyClass: 
#     pass

# obj1 = MyClass()
# obj2 = MyClass()

# obj1.x = 10
# obj1.y = 20
# obj2.x = 30
# obj2.y = 40

# print("obj1 : x : {0} , obj1: y : {1}".format(obj1.x,obj1.y))
# print("obj2 : x : {0} , obj2: y : {1}".format(obj2.x,obj2.y))

# Adding attributes and methods from inner to class

class MyClass:
    def myMethod(self,x,y): #Normal method
        self.x = x
        self.y = y


obj1 = MyClass()
obj2 = MyClass()
obj1.myMethod(10,20) # Need to active because of normal method
obj2.myMethod(20,30)

print(obj1.x, obj1.y)
print(obj2.x, obj2.y)