#X mode doesn't read,write and append, but only open files and creates files if isn't file

filePtr = open("textx.txt", "x")
# print(filePtr)

###With statement can auto close file if program causes error.We don't need to write close().

"""with open("textx.txt", "r") as file:
    if file:
        contents = file.read()
        print(contents)
        print(file.tell())
    else:
        print("something wrong")"""


#file.tell() It tells you the current position of the file pointer.

# The above code is opening a file in read and write mode. It is checking if the file is open or not.
# If the file is open, it is printing the file pointer position. Then it is reading the file and
# printing the file pointer position. Then it is writing to the file and printing the file pointer
# position.
with open("textx.txt", "r+") as file:
    if file:
        print("The file pointer at byte",file.tell())
        file.read()
        print("The file pointer at byte",file.tell())
        file.write("Hello")
        print("The file pointer at byte",file.tell())

        
    else:
        print("something wrong")