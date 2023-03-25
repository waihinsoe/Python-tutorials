class Animal:
    color = "yellow"
    age = "2"
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

dObj = Dog()

dObj.color = "red"
dObj.age = "4"
print(dObj.color)
print(dObj.age)

#Multiple Inheritance
class Parent:
    def own(self):
        print("This is from parent.")

class Uncle:
    def uncle(self):
        print("This is from uncle.")

class Aunt:
    def aunt(self):
        print("This is from aunt")

class Son(Parent, Uncle, Aunt):
    def son(self):
        print("This is mine.")
        
Sobj = Son()

Sobj.aunt()
Sobj.own()        
Sobj.son()
Sobj.uncle()

#Multilevel Inheritance
class Parent:
    def own(self):
        print("This is from parent.")

class Uncle(Parent):
    def uncle(self):
        print("This is from uncle.")

class Child(Uncle):
    def son(self):
        print("This is mine.")
        
Cobj = Child()

Cobj.own()
Cobj.son()
Cobj.uncle()

# Base1 Base2 Derived
class Base1:
    def multi(self,a,b):
        return a*b
class Base2(Base1):
    def adding(self,a,b):
        return a+b
class Derived(Base2):
    def sub(self,a,b):
        return a-b
obj = Derived()

print("From base1 :",obj.multi(10,23))
print("From base2 :",obj.adding(20,12))
print("From Derived :",obj.sub(30,10))
