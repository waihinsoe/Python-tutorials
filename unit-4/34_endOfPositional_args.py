#end of positional argument eg. *
#Keyword only arguments  eg.  d = 5
#Keyword argument        eg. **


def myFun(a,b,*,c): #Positional argument can't follow behind end of positional argument.
    print(a)
    print(b)
    print(c)
    
myFun(1,2,c=3)


def myDis(**key): # Keyword argument outputs variables with dis. 
    print(key)

myDis(a=1,b=2,c=3,d=4)

#We can't use together end of positional and keyword arguments.
#But can use by adding keyword only argument between them.Like that;;;
def myWorld(a,b,*,koa,**ke):
    print(a)
    print(b)
    print(koa)
    print(ke)

myWorld(a=1,b=2,c=3,koa=4)