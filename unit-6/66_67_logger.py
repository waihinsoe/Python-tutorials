def logger(fn):
    from functools import wraps
    from datetime import datetime, timezone
    
    @wraps(fn)
    
    def inner(*args, **kwargs):
       dt = datetime.now(timezone.utc) 
       result = fn(*args, **kwargs)
       print("{0} called  {1} :  recent data : {2}".format(dt,fn.__name__,result))
       
       return result
   
    return inner

@logger
def myFun1(x,y):
    """from function one"""
    return x + y
myFun1(20,30)

@logger
def myFun2(x,y):
    """from function two"""
    return x

myFun2(3,7)