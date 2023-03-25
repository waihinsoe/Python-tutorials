#String
#enumerate
# s = "waihinsoe"
# i=0
# for a in s:
#     print(i,a)
#     i+=1

# s = "waihinsoe"
# for a,c in enumerate(s):
#     print(a,c)

# row = int(input("please enter row :>"))
# for i in range(row):
#     for a in range(row,i,-1):
#         print(a,end=(""))
        
#     print("")

row = int(input("please enter row"))

for i in range(5,row):
    for a in range(i,0,-1):
        print(a,end="")
    print("")