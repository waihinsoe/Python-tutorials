def fact(n):
    print("calculating n:",n)
    return 1 if n<2 else n*fact(n-1) #recursive

results =list(map(fact , range(6))) 

print(results)

for i in results:
    print(i)
    
for x in results:
    print(x)
    
    
print("###########################################################################")

list1 = [1,2,3,4,5,6,7,8]
list2 = [10,20,30,40,50,60]

result = list(map(lambda x,y:x+y,list1,list2))
print(result)

for i in result:
    print(i)