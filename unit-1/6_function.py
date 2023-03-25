#function
#########Standard library function

# from math import sqrt
# import math
# ls= [1,2,3,4,5]
# print('The length of ls is ',len(ls))
# data = int(input("Please enter something :"))
# print("The square root of {} is {}".format(data,sqrt(data)))

# print("The value of pi is ",math.pi)

# print("The value of {} is {}".format(data,math.exp(data)))

# print('The value of {} is {}'.format(data,hex(data)))



#######Programmer Defined function 
# def hello(a,b): a,b=>parameter
#     print(hello(2,3)) 2,3=>positional argument

a = int(input("Please enter first number :"))
b = int(input('Please enter second number :'))

def add(a,b):
    return a+b

def sub(a,b):
     return a-b

def multi(a,b):
     return a*b

def divide(a,b):
     return a/b

print(add(a,b))
print(sub(a,b))
print(multi(a,b))
print(divide(a,b))