#QUESTION 07
"""You have just entered college and would like to buy a laptop of cost,'cost'.
Your monthly allowance is allowance, and you can save a fraction 'sf' of it every month.
Every month, you put your savings in a bank account that gives you a monthly rate of interest r (interest is compounded).
Determine after how many months you will be able to purchase the laptop and the amount of savings that will remain after purchase.
For laptop cost, take the input from the user and Take allowance as Rs 20,000, your saving fraction sf is 0.1,
and the rate of interest r is 0.5."""

#CODE:
#Defining function for Required Amount Calculation:-
def total_amount(p,r,t):
    global total_amount_val
    total_amount_val=(p*(1+r)**t)
    return total_amount_val


#Taking input and assigning values to variables.
cost=int(input("Cost of Laptop:-"))
allowance=20000
sf=0.1
r=0.5
t=1 #represents 1 month
#As, first month is taken up in saving amount for putting money in compund interest.
if cost<=2000:
    print(1)
else:
    total_amount(allowance*0.1,r,t)
    month_count=2
    while total_amount_val+allowance*sf<cost:
        p=total_amount_val+allowance*sf
        month_count+=1
        total_amount(p,r,t)
    print("Number of Months:-",month_count,"months")
remain_sav=(total_amount_val+allowance*sf)-cost
print("Remaining Saving:-",remain_sav)