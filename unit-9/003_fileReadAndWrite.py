#readline() returns with string
#readlines() returns with list

# file = open("content2.txt","r")

# if file:
#     print("Success of opening file")
#     data = file.readlines()
#     print(data)
#     file.close()
#     file = open("content2.txt","r")
#     print("Reading with readlines")
#     content = file.readline()
#     print(content)
#     file.close()
# else:
#     print("Error")  
    
###File writeMethod deletes current things and replaces new things.
###File appendMethod doesn't delete them and appends new things.
file = open("content2.txt","w")
text = "Hello I am wai Hin Soe"

if file:
    print("File opening is success")
    file.write(text)
else:
    print("something wrong catch error")
