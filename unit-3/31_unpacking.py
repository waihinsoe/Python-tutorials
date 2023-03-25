#Unpacking
###Extended unpacking

# a,*b,c,d = "waihinsoe332004"# *  Can unpack list , tuple and string
# print(a)
# print(b)
# print(c)
# print(d)

# li_1 = [1,2,3,4]
# li_2 = [5,6,7,8]
# li = [*li_1,*li_2]
# print(li)

#####Another way unpacking
a,*b,(c,*d,e),[x,*y,z] = [1,2,3,'waihinsoe','hmwecherryoo']
print(a)
print(b)
print(c)
print(d)
print(e)
print(x)
print(y)
print(z)

####Index unpacking

Index = [1,2,3,4,'waihin','soe']

print(Index[0])
print(Index[0:-1])
print(Index[4][2])