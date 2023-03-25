from socket import gaierror
import myModule

myModule.fibo(10)
print(myModule.listFibo(100)) #Can Use

del globals() ['myModule'] #Module delete
fibo(300) #Can't use