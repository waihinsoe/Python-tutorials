# number = int(input("please enter number :"))

# def checking(number):
#     xy = number
#     palindrome = ''
    
#     print("original number :",number)

#     while number > 0:
#         x = number%10
#         number = int(number/10)
#         palindrome +=str(x)
#     if xy == int(palindrome):
#         print("Yes, given number is palindrome number")
#     else:
#         print("No,given number is not palindrome number")
    
# checking(number)






# number = int(input("please enter number :"))

# def checking(number):
#     xy = number
#     palindrome =0
    
#     print("original number :",number)

#     while number > 0:
#         remainder = number%10
#         palindrome = (palindrome*10) + remainder
#         number = int(number/10)
#     if xy == palindrome:
#         print("Yes, given number is palindrome number")
#     else:
#         print("No,given number is not palindrome number")
    
# checking(number)

# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]

# list3 = []

# for i in list1:
#     if i%2 != 0:
#         list3.append(i)
# for x in list2:
#     if x%2 == 0:
#         list3.append(x)
        
# print("result list :",list3)

# given_num = 7536

# def extract(num):
#     while num > 0:
#         digit = num%10
#         num = int(num/10)
#         print(digit,end=" ")

# extract(given_num)

# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j,end=" ")
#     print("\t\t")

# amount = 5
# star = amount
# for i in range(amount):
#     for j in range(star):
#         print(end="*")
#     star -=1
#     print(" ")

# for i in range(6,0,-1):
#     for j in range(0,i-1):
#         print(end="*")
#     print(" ")

# base = int(input("Please enter base :"))
# exponent = int(input("Please enter exponent"))

# if base and exponent:
#     def power(base,exponent):
#         return base**exponent
#     result = power(base,exponent)
#     print("base raises to power of 4 is :",result)
# else: 
#     print("something wrong please fill all input!!!!")

# base = 5
# exponent = 4

# result = 1

# while exponent > 0:
#     result = result * base
#     exponent -=1

# print("base raises to power of 4 is : ",result)

# from turtle import position


# number = int(input("Please enter number :"))
# def expand(number):
#     print("original number :>",number)
#     num_for_loop = number
#     numList = []
#     position_num = 1
#     while num_for_loop > 0:
#         remainder = num_for_loop % 10
#         expand_num = remainder*position_num
#         numList.append(expand_num)
#         position_num *= 10
#         num_for_loop = int(num_for_loop/10)
    
#     x,*y,z = numList
#     x,y,z = z,y,x
#     print(x,"+",y,"+",z)
    
    

# expand(number)





