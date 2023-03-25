#Higher order function

def myFun(fn,*args,**kwargs):
    return fn(*args,**kwargs)

value = myFun(lambda x,y: x+y,23,y=20)

print(value)