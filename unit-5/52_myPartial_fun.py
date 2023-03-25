# def myFun(x,y,z):
#     print(x,y,z)

# def pFn(yy,zz):
#     return myFun(10,yy,zz)

# pFn(100,200)
##########################################################

from functools import partial


def myFun(x,y,z):
    x += 11
    y += 11
    z += 11
    print(x,y,z)

newFun = partial(myFun,10)

newFun(100,200)