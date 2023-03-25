x= 10
k=9
a=1
b=8
for i in range(10):
    for j in range(x):
        print(end="  ")
    x -=1
    for y in range(1,a):
        print(y,end=" ")
    a += 1
    for i in range(i-1,0,-1):
        print(i,end=" ")
    print(" ")
    
for i in range(1,11):
    for i in range(i+1):
        print(end="  ")
    for g in range(1,k):
        print(g,end=" ")
    k-=1
    print(" ")