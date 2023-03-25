def decToHexa (n): #decimal will pass
    hexa = ['0']*10
    
    i = 0 #counter
    
    while (n != 0):
        temp = 0
        temp  = n%16
        if (temp < 10):
            hexa[i] = chr(temp+48)
            i +=1
        else: 
            hexa[i] = chr(temp+55)
            i+=1
        n = int(n/16)
    
    x = i -1
    while(x >= 0):
        print(hexa[x],end="")
        x -=1

def binaryToDec (b): #binary will pass
    num = b
    dec = 0
    base = 1 # 2*2^0
    temp = num
    while (temp):
        digit = temp%10
        temp = int(temp/10)
        dec += digit *base
        base = base*2
    return dec

decimal = binaryToDec(int(input("please enter binary number : ")))  

print("decimal",decimal) 

decToHexa(decimal)