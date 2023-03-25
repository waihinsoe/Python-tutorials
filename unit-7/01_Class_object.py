class Myclass: #attributes  behavior
    pass

obj1 = Myclass()
obj2 = Myclass()

print(obj1)
print(obj2)

if obj1 is obj2:
    print("They are same")
else:
    print("They are not same.")