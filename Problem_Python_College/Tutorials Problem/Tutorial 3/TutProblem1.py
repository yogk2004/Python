x=int(input())
for a in range(x):
    for b in range(a,x):
        print("*", end="")
    for y in range(0,a):
        print(" ",end="")
    for b in range(0,a):
        print(" ", end="")
    for c in range(a,x):
        print("*",end="")
    print()
for d in range(x):
    for e in range(d+1):
        print("*", end="")
    for g in range(d,x-1):
        print(' ',end="")
    for g in range(d,x-1):
        print(' ',end="")
    for c in range(d+1):
        print("*",end="")
    print()     