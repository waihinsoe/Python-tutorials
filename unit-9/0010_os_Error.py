#Error Handling
try:
    file = open("hello.txt","r")
# It's catching the error and printing it.
except Exception as err:
    print("OSError : {0}".format(err))
# It's running no matter what.
finally:
    print("I don't care if it's true or false.I'm running,Ok")
    