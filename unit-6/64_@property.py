from tkinter.messagebox import RETRY


def myDec_1 (fn):
    def inner():
        print("running decorator_1")
        return fn()
    return inner

def myDec_2(fn):
    def inner():
        print("running decorator_2")
        return fn()
    return inner


@myDec_1
@myDec_2
def myFun():
    print("running myFun")
    
myFun()
  
# result = myDec_1(myDec_2(myFun))
# result()