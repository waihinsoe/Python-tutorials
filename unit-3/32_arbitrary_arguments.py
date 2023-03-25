#Arbitrary arguments
def myFun(a,b,c,*args):#We can't use positional arguments behind the arbitrary arguments
    print(a)        
    print(b)
    print(c)
    print(args)
myFun(1,2,3,4,5,6)

def avg(*args):
    length = len(args)
    total = sum(args)
    if length == 0:
        return 0
    else:
        return total/length

print(avg())