#Returning function form a function 

# def  square(a):
#     return a**2

# def cube(b):
#     return b**3

# def Num(number):
#     if number == 1:
#         return square
#     else:
#         return cube

# sq = Num(1)
# cu = Num(2)
# print(sq(2))
# print(cu(4))

#function passing to a function
def square(a):
    return a**2

def cube(b):
    return b**3

def funToFun(fun,n): #function name,Number some
    return fun(n) 

a = funToFun(square,4)
b =funToFun(cube,8)
print("Calling square function :",a)
print("Calling cube function :",b)