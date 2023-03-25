#lesson for loop

# i=0
# while i < 5 :
#     print(i)
#     i+=1


# l = [(1,2),(3,4),(5,6),(6,7)] #j => unpacking
# for i,j in l:
#     print(i,j)

for i in range(7):
    print("############")
    try :
        z=i/(i-3)
        print(z)
    except ZeroDivisionError:
        print("Divided by zero")
    finally:
        print("always run")
    print(i)

# for i in range(1,5):
#     if i%3 ==0:
#         print("multiple of 3 found")
#         break
#     else:
#         print("no multiple of 3")    