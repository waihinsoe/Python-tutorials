def counter(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print("function {} is called {}".format(fn.__name__,count))
        return fn(*args, **kwargs)
    return inner

def add(a, b):
    """adding two value using decorator"""
    print(a+b)
    
def sub(a, b):
    """sub two value using decorator"""
    print(a-b)
       
resultAdd = counter(add)
resultSub = counter(sub)
resultAdd(10,20)
resultSub(30,20)
resultAdd(30,40)
resultSub(50,20)
resultAdd(50,60)
resultSub(60,30)
