#Class built in function
#getattr(obj, name)
#setattr(obj, name, value)
#delattr(obj, name)
#hasattr(obj, name)

class MyClass:
    def __init__(self,name, age, id) -> None:
        self.name = name
        self.age = age
        self.id  = id

obj = MyClass("wai",18, 121053)
print(getattr(obj, 'name' ))
setattr(obj, 'age', 20)
print(getattr(obj, 'age'))
delattr(obj, 'age')
print(hasattr(obj, 'age'))