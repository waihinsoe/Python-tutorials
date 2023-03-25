#least recently used => lru_cache
#built in decorator
from functools import lru_cache

@lru_cache(maxsize=3)
def fibo(n):
    print("Calculating {0}".format(n))
    return 1 if n<3 else fibo(n-1)+fibo(n-2)

print(fibo(5))
print(fibo(10))
print(fibo(100))