#Encapsulation private

"""class Parent:
    def __init__(self,age):
        self.__age = age

class Child(Parent):
    def modify(self,input):
        self.__age = input
        return self.__age
    def get_data(self):
        
        print(self.__age)

obj = Child(30)
obj.modify(100)
obj.get_data()
print(obj.__dict__)"""

# print(p.__dict__)
# print(p.__age) #can't work

class Animal:
    def __init__(self, name, color, age, behavior) -> None:
        self.__name = name
        self.__color = color
        self.__age = age
        self.__behavior = behavior

class Dog(Animal):
    def dModify(self, name, color, age, behavior):
        self.__name = name
        self.__color = color
        self.__age = age
        self.__behavior = behavior
    def dGet_data(self):
        print(self.__name, self.__color, self.__age, self.__behavior)


obj = Dog("Mi War","red", 4, "sleep")
obj.dModify("Gyote Kyar","yellow",6,"bark")
obj.dGet_data()

        