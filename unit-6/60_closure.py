#Closure

# def myFun():
#     data = 'I am belong to myFun'
#     def inner():
#         print(data)
#     return inner

# obj = myFun()
# del myFun
# obj()

def myFun(n):
    def adding(data):
        return data+n
    return adding

add10 = myFun(10)
add20 = myFun(20)
print("adding 10 :",add10(20))
print("adding 20 :",add20(20))
print("adding add10 and add20 :",add10(add20(5))) 