# def myFun(a:<expression>,b:<expression>)->return <expression>:

# function annotation 

#annotation -> parameters and return of a function

#docString -> body of a function

""" def myFun(a : 'annotation of a',b : 'annotation of b')->'return of function':
     This is body expression for myFun 
    return a*b

print(myFun.__annotations__)
print(myFun.__doc__) """

x=2
y=5
def myFun(a:'something value from funCall',b:'something value from funCall')->'b + multiply by '+str(max(x,y))+'times':
    """ doc.... will return multiply by  value of max"""
    return b+a*max(x,y)

myFun(3,5)
print(myFun.__annotations__)
print(myFun.__doc__)