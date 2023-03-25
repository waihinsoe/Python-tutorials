from datetime import date


def timer(fn):
    import time
    from functools import wraps
    
    @wraps(fn)
    def inner(*args, **kwargs):
        st = time.perf_counter()
        result = fn(*args, **kwargs)
        en = time.perf_counter()
        avTime = en - st
        print("function {0} worked for {1} times . result {2}".format(fn.__name__, avTime, result))
        return result
    return inner

@timer
def matt(x):
    for i in range(100):
        x += i
    return x

matt(0)