#What is crud?
# c=> create r=> read u => update d =>delete
#It's tow ways
#Build in 
#Manually
 # class method // outside hold object


class Myclass:
    def __init__(self) -> None:
        self.name = "Wai"
        self.age = "18"
        self.hobby = "Artificial intelligent"
    def update(self):
        self.name = "G2"
        self.age = "19"
        self.hobby = "Web development"

obj1 = Myclass()
obj2 = Myclass()
print("before update")
print(obj1.name, obj1.age, obj1.hobby)
print(obj2.name, obj2.age, obj2.hobby)

# obj1.name = "Hin"
# obj1.age = "20"
# obj1.hobby = "Hacking"

# obj2.name = "Soe"
# obj2.age = "21"
# obj2.hobby = "Data science"
obj1.update()
obj2.update()
print("After update")
print(obj1.name, obj1.age, obj1.hobby)
print(obj2.name, obj2.age, obj2.hobby)

