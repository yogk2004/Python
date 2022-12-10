n= [1,2,3,4,5,6,7,8]
for x in n:
    if x==1:
        print("1")
    elif x==2:
        continue
    else:
        for z in range(2,x):
            if (x%z==0):
                print(x)
                break