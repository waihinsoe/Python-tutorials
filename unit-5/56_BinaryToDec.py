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

print(binaryToDec(101010))