from functools import partial
from tokenize import Exponent

# def myFun(x,y,*args,x1,y1,**kwargs):
#     print(x,y,args,x1,y1,kwargs)

# newFun = partial(myFun,10,x1 = "hello")

# newFun(20,30,40,y1 = "test", aa=50,bb=60,cc=70)

def myFun(base , exponent):
    return base**exponent

sq = partial(myFun,exponent = 2)

cu = partial(myFun, exponent = 3)

print(sq(2))
print(cu(4))
print("testing for base with 5 and expo 3 :",cu(base = 5))
