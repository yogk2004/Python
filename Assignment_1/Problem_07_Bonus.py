#QUESTION 7 (BONUS):-
""" Suppose you want to buy the laptop in fewer months. As the interest rate is not in your control,
you can only change the saving fraction. Determine the savings rate needed for different numbers
of months for purchasing the laptop, starting from the number of months determined earlier. """

#CODE:
#Defining Function for Counting Looping Of mathematical formula for finding "Saving Rate".
def loop_funcX(x,r):
    x=(x*(r+1)+1)
    return x

#Taking Input and Calculating Time:-
time=int(input("Number of Months:- "))
cost=float(input("Cost of Laptop:- "))
r=0.5
x=1
allowance=20000
for i in range (time-1):
    x=loop_funcX(x,r)
print("Saving Rate Needed:-",((cost/(allowance*x)))*100,"% of allowance")