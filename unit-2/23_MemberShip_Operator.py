#Membership operator => in / not in


# list1 = [1,2,3,4,5,"w"]
# list2 = [6,7,8,9]
# print(1 in list1)
# if "w" in list1:
#     print("W is in list1")
# else:
#     print("W is not in list1")

# print(2 not in list1)

# x = 34 
# y = 23

# myList = [23,45,46,43,56,78,89]

# if x in myList:
#     print("x is in given myList :")
# else:
#     print("x is not in given myList")

# if y not in myList:
#     print("y is not in given list")
# else: 
#     print("y present in given list")


list1 = [1,2,3,4,5,6]
list2 = [7,1,8,9,12]

def overlap(list1,list2):
    c = 0
    d = 0
    for i in list1:
        c+=1
    for i in list2:
        d +=1
    for i in range(0,c):
        for j in range(0,d):
            if list1[i]== list2[j]:
                return 1
    return 0

if (overlap(list1,list2)):
    print('list1 and list2 are overlap')
else: 
    print("list1 and list2 are not overlap")
