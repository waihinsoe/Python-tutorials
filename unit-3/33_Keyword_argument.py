#Positional arguments
#Arbitrary arguments
#Keyword only arguments
#End of positional argument

def myFun(a,b,*c,d): ### d is keyword only argument
    print(a)         ## Keyword only argument can follow behind the arbitrary arguments
    print(b)
    print(c)
    print(d)
myFun(1,2,3,4,5,6,d=7)

def hello(*a,b,c):
    print(a)
    print(b)
    print(c)

hello(1,2,3,c=4,b="waihin")