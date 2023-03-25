#While loop
# a = 20 
# b = 20
# while a<b: # This false
#     print('{} Hello I am Waihinsoe'.format(a)) # This stop
#     a +=1
# print('Nothing do!') # this do


#Break and continue

# for var in 'waihinsoe':
#     if var == "i":
#         continue
#     print(var)
# print("_______________________ending")

ls= [23,45,67,64]
data = 99
found = False
index = 0
#     5     <  5
while index < len(ls): #true
    if ls[index] == 99: 
        found = True
        break
    index += 1

if not found:
    ls.append(99)
print(ls)

