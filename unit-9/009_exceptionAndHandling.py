#Exception and Handling

# Trying to open the file.
try:
    file = open("contentx.txt","r")
# Catching the exception and printing the message.
except:
    print("cannot open")
# Running the code if the exception is not raised.
else: 
    print("File is running")
