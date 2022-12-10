number = int(input("Enter a number: "))
NewNumber=int(number/2)
# prime numbers are greater than 1
if number > 1:
   # check for factors
    for i in range(2,NewNumber):
        if (number % i) == 0:
           print(number,"is not a prime number")
           print(i,"times",number//i,"is",number)
           break
    else:
        print(number,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
    print(number,"is not a prime number")
print(((5*5-5)**2+1)/4)