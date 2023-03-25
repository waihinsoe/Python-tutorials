#Build in attributes
#__dict__ shows information of class with dictionary
#__doc__
#__name__
#__module__
#__bases__

class MyClass:
    variable = "Programming"
    def active():
        print(f'hello from {MyClass.variable}')

x = MyClass.__dict__
for key, value in (x.items()):
    print("{0} : {1}".format(key, value))
