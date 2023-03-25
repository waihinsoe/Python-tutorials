#In normal value,if variables are different name and same value , are same location
#But list , not same location

a = 20 
b = 20

print(id(a),id(b))
if a is b:
    print("They are same location")
else:
    print("They are not same location")
    
c = [1,2,3,4,5]
d = [1,2,3,4,5]

print(id(c),id(d))
print(c is d)

if c is d:
    print("They are same location")
else:
    print("They are not same location")
    
if c == d:
    print('They are same value')
else: 
    print("They are not same location")
    
    
#Namespace
#Global namespace
#local namespace
#build in namespace

x = 30 #global namespace 
def gloName():
    return int(x)+3
print(gloName())

def locName():
    y = 40 #local Namespace
    return print(y)
id(x)# build in name space

locName()