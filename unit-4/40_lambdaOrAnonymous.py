#Anonymous function
#Lambda expression or anonymous function

x=lambda x,*args,y,**kwargs:(x,args,y,kwargs)
print(x(1,'a','b',y=10,i=3,j=5,k=8,c=12,v=34))