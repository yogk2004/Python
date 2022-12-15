#QUESTION 07
"""You have just entered college and would like to buy a laptop of cost,'cost'.
Your monthly allowance is allowance, and you can save a fraction 'sf' of it every month.
Every month, you put your savings in a bank account that gives you a monthly rate of interest r (interest is compounded).
Determine after how many months you will be able to purchase the laptop and the amount of savings that will remain after purchase.
For laptop cost, take the input from the user and Take allowance as Rs 20,000, your saving fraction sf is 0.1,
and the rate of interest r is 0.5."""

#CODE:
#Defining function for Required Time calculation:-
def total_amount(p,r):
    global total_amount
    total_amount=(p*(1+r))
    