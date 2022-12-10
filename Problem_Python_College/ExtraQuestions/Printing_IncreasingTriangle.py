'''n=int(input("Height and Breath of Triangle:"))
for i in range(1,n):
    print("*"*i , end="")
    print()'''

n=int(input("Height and Breath of Triangle:"))
for i in range(n):
    for j in range(i+1):
        print("*", end="")