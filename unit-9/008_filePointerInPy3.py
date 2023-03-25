import os

with open("content.txt", "a") as file:
    if file:
        print("current position",file.tell())
        file.seek(5, os.SEEK_SET)
        print("moving 5 current position",file.tell())
        file.seek(0, os.SEEK_END)
        print("current position",file.tell())
        file.seek(file.tell()-5, os.SEEK_SET)
        print("Moving -5 current position",file.tell())
    else:
        print("something wrong")
