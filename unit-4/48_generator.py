# #Generator
# from re import X


# def myFun():
#     return x #terminate

# def myGen():
#     yield g
#     yield g+1
#     yield g+2 #suspend

def myGen():
    """
    It returns a generator object.
    """
    data = 10
    yield data
    yield data+1
    yield data+2
    yield data+3
    yield data+4
    yield data+5
    
results = myGen()

# print(results)
# print(results.__next__())
# print(results.__next__())
# print(results.__next__())
# print(results.__next__())
# print(results.__next__())
# print(results.__next__())

#######OR##########
for i in results:
    print(i)
print("############################################################################")

###################################################3

def Gen():
    data = 1 
    while data < 10:
        square = data*data
        yield square
        data += 1
        

gResults = Gen()

print(gResults)

for i in gResults:
    print(i)