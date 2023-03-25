def memoize(fibo):
    cache = {1:1,2:1}
    def inner(n):
        if n not in cache:
            cache[n] = fibo(n)
        return cache[n]
    return inner

# @memoize
def fibo(n):
    print("Calculating n :",n)
    return 1 if n<3 else fibo(n-1)+fibo(n-2)

fibo = memoize(fibo)
print(fibo(7))
print(fibo(5))

