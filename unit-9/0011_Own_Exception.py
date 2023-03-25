#raise
try:
    data = int(input("please enter a number :"))
    if data == 10:
        # Raising an exception.
        raise ZeroDivisionError
    else:
        raise TypeError
except ZeroDivisionError:
    print("From Zero Division Error")
except TypeError:
    print("From TypeError")
    
#To know what are ZeroDivisionError Class?
try:
    a = 10/0
except ZeroDivisionError as err:
    print(err)
    
print("################################################################")


# It creates a class called MyExcept, and two subclasses of it called ValueError and NameError.
class MyExcept(Exception):
    pass
class ValueError(MyExcept):
    pass
class NameError(MyExcept):
    pass

try:
    a = 10
    b = 20
    if a is b:
        raise ValueError
    else:
        raise NameError

except ValueError:
    print("Value Error")
except NameError:
    print("NameError")

    