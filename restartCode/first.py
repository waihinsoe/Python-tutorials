def myFun(a, b, c, *args, d, e, f):
    print(a)
    print(b)
    print(c)
    print(args)
    print(d)
    print(e)
    print(f)


myFun(1, 2, 3, 4, 5, 6, 7, 8, d="hehe", e=12, f=23)
