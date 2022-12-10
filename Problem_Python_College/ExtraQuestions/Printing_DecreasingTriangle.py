'''a=int(input("Base and Height of Triangle:"))
for i in range(a):
    for j in range(a-i):
        print("*", end="")
    print()'''

a=int(input("Base and Height of Triangle:"))
for i in range(a):
    for j in range(i,a):
        print("*", end="")
    print()