def DecToBinary(n): #Decimal number will pass
    """
    It takes a decimal number and converts it to binary
    
    :param n: The decimal number that will be converted to binary
    """
    binary = [0]*n
    i = 0 #counter
    

    while (n > 0):
        binary[i] = n%2
        n =int(n/2) 
        i += 1
    
    for x in range(i-1,-1,-1):
        print(binary[x],end="")


decimalNumber = int(input("please enter decimal number : "))
DecToBinary(decimalNumber)
        
    