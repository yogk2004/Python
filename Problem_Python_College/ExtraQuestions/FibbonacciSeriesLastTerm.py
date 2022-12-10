no_terms=int(input())

#Defining Function
def Fibbonacci_Sum(integer):
    if integer==1:
        return(0)
    elif integer==2:
        return(1)
    else:
        return (Fibbonacci_Sum(integer-1)+Fibbonacci_Sum(integer-2))

#Calling Function
print(Fibbonacci_Sum(no_terms))