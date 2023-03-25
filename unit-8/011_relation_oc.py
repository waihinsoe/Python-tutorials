# isinstance
# issubclass

class MyClass:
    pass

class YourClass(MyClass):
    pass

print(issubclass(YourClass, MyClass))

obj = YourClass()

print(isinstance(obj, YourClass))
print(isinstance(obj, MyClass))
    