#QUESTION 09
"""The demand for an item in the market (in terms of the number of items) decreases as the price (p) of the items increases.
On the other hand, the supply of the item increases as the price increases (as producers expect to make more profit).
Suppose the demand and supply changes as follows with price:
 
Demand function, D is:  ln D(p) = a - b*p  (i.e. D(p) is e to the power of rhs)
Supply function, S is: ln S(p) = c + d*p 

An equilibrium is achieved when demand and supply match (approximately) - this is a basic economics theory.
Determine at what price an equilibrium will be reached, and output the equilibrium price and the number of items
produced/bought at this equilibrium. Given a minimum price, find at what price an equilibrium is found, if it exists.
(If no solution is possible - print that).Iterate by starting with the minimum price and increasing the price by 5% every time
(so your equilibrium will not be precise), to find the equilibrium.
Your program should print the equilibrium price, and the demand and supply at that price.
For this take a, b, c, d as 10, 1.05, 1, 1.06.  You can assume that the minimum price as 1.0."""

#CODE:
#Defining function for Demand and Supply:-
def Demand_supply_value(a,b,c,d,price):

    D_p=(2.7182818)**(a-b*price)
    S_p=c+d*price
    return D_p , S_p

#Taking Input:
a=float(input("Enter value of a:- "))
b=float(input("Enter value of b:- "))
c=float(input("Enter value of c:- "))
d=float(input("Enter value of d:- "))

price=1.0
x,y=Demand_supply_value(a,b,c,d,price)
while x>=y:
    #Incresing input by 5% every time.
    price=price+(price*5/100)
    x,y=Demand_supply_value(a,b,c,d,price)
print("The Needed Value of 'p' is:-",(price*100/105))
r,g=Demand_supply_value(a,b,c,d,price*100/105)
print("The Value of Demand:-",r)
print("The Value of Supply:-",g)
#NOTE:- As, the input in the above Function is going at an increase rate of 5% (specified in Question).
#So, I am printing the value of 'Price' after which the Supply surpasses the Demand and
# also their values as specified in comment of Assignment by Mr. Pankaj Jalote Sir.