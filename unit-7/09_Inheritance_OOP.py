#Inheritance 
 #Multiple inheritance
 #MultiLevel inheritance

class Animal:
    def eat(self):
        print("Animals are eating")

class dog(Animal):
    def bitch(self):
        print("Bitch are running")

obj = dog()
obj.bitch()
obj.eat()

class Parent:
    def own(self):
        print("We have many jewels")

class Child(Parent):
    def son(self):
        print("so so poor")

cobj = Child()
cobj.own()
cobj.son()