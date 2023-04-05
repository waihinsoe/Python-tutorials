# Special operator
# Identity operator => is / is not  (Memory allocation)
# Membership operator

# a = 10
# b =  10
# print (id(a))
# print (id(b))

# if a is b:
#     print("They are same location :")
# else:
#     print("They are not same location")

# b = 20
# if a is b:
#     print("2 They are same location")
# else:
#     print("2 They are not same location")

# a = 10
# b = 10
# c = a is not b
# print("They are same location :", c)

# x = 20
# y = 20
# print("They are same location :",c)

string1 = "waihinsoe"
string2 = "waihinsoe"

print(id(string1))
print(id(string2))
if string1 is string2:
    print("They are same location :")
else:
    print("They are not same location")

if string1 == string2:
    print("They are same")
else:
    print("They are not same")
