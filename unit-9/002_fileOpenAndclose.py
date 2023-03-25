file = open("content.txt","r")

if file:
    print("Success of opening file")
    data = file.read(10)
    print(data)
    
else:
    print("Error")  
    
file.close()
