#Variable are Memory Reference
#How they are allocated in program memory
#Variable are memory reference
#What is memory reference
#What is memory address in C

#id()
#Different between Python and C
#hex()

#####################################################################################

#data = 0x1008 (reference) -->> 10(object)
#Variable are Memory Reference.....

a = 10
b = 10
print(hex(id(a)))
print(hex(id(b)))

if id(a) == id(b):
    print("They are same memory address ",id(a))
else: 
    print("They are not same")