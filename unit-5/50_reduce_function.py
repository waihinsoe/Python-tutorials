from ast import Lambda
import functools

list =[1,2,3,4,5,6,7]


print('The sum of all elements is :',end="")
print((functools.reduce(lambda a,b: a+b,list)))

print("The multiply of all elements is :",end="")
print((functools.reduce(lambda a,b: a*b,list)))

print("The largest number from list :",end="")
print(functools.reduce(lambda a,b: a if a>b else b,list))