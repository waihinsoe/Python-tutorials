#list method and function
#remove / pop / del
#append 

myList = ['myanmar','english','math','computer science']

myList[-1]= 'hello world'

print(myList)

myList.remove("math") #work with index'value
print("after using remove method\n")
print(myList)

myList.pop(2) #work with index
print("after using pop method\n")
print(myList)

del myList[0] #del not function/method , is key
print('after using del')
print(myList)

myList.append("data structure")
print(myList)

print(len(myList))