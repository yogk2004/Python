number=input()
digits=len(number)
sum=0
for i in range(digits):
    no_digit=int(number[i])
    sum+=(no_digit)**3
print(sum)