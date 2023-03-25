import imp


#This is module delete unit
def print_info(header, info):
    print("***********{0}*********".format(header))
    for key, value in info.items():
        print(key, value)
    print("End of information")


print_info("Global function", globals())
print(__name__)

if __name__ == "__main__":
    print("__name__ change into __main__")
else: 
    print("__name__ is not equal __main__")
    