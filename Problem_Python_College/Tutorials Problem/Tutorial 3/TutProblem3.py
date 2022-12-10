number=int(input("Enter a number: "))

def Function1(number):
    if number>=0:
        for i in range(1,number):
            if number%i==0:
                print(i,end=" ")
        print(number)
        number=int(input("Enter a number: "))
        Function1(number)

Function1(number)