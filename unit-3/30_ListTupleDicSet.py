#List  (ordered)
#Tuple (ordered)
#Dictionary (unordered)
#Set   (unordered)

# li = [1,2,3,4,5]
# print(li[2]) #work

# tu = (1,2,3,4,5,6)
# print(tu[3]) #work

# se = {1,2,3,4,5}
# print(se[2]) #not work

# di = {'a':1,'b':2,'c':3,'d':4}
# print(di['a']) #not work

#
# ###########unpacking

a,b,c = [1,2,3]
print(a,b,c)

[a,b,c] = 1,2,3
print(a,b,c)

(a,b,c) = [5,6,7]
print(a,b,c)

x,y,z = {1,2,3}
print(x,y,z)

(a,b,c) = 'wai'
print(a,b,c)

dset = {1,2,3,4,5,6}
print(dset)

dset_2 = {'a','b','c','d','e'}
print(dset_2) # not order with string