def myFun(x,y,z=10,*,kw1,kw2=12):
    return x+y

print(myFun.__name__)#name
print(myFun.__defaults__)#positional argument
print(myFun.__kwdefaults__)# keyword only argument
print(myFun.__code__) # code is object so we can use methods and properties;
print(myFun.__code__.co_varnames)# output variables
print(myFun.__code__.co_argcount)# count argument in function: for positional argument

#About inspect module
import math
import inspect
from inspect import isfunction,ismethod
#getsource
print(inspect.getsource(myFun))
#getcomments
print(inspect.getcomments(myFun))

#different between function and method 
# class hello:
#     myFun()# method
    
# myFun()#function
print("checking is function",isfunction(myFun))
print("checking is ismethod",ismethod(myFun))

#getmodule
print(inspect.getmodule(myFun))
print(inspect.getmodule(math.sin))
print(inspect.getmodule(ismethod))
print(inspect.getmodule(print))