def multiply(a,b,c):# Here, the default value should come after. 
    return a*b*c
list=[]
n=int(input())
for i in range(n):
    list.append(int(input()))
a=list[0]
b=list[1]
c=1
if n==3:
    c=list[2]

print(multiply(a,b,c))