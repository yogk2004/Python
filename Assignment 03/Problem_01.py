#Question 01 :-
"""Print the pattern given below using recursion - no loops are allowed.
You are given a value n - print a diamond which will have 2n-1 rows, and 2n columns,
as shown in the figure. (In the top row print n+n stars, in the next (n-1) stars on left and
right and 2 blanks in the middle, and so on till you have 1 star each on left and right; then you reverse this)."""

#CODE:-
# Recursion based Code for upper-half pattern printing.
def upperhf(a,b):
    if (2<=a-b):
        print("*"*(a-b) + " "*(2*b-2) + "*"*(a-b))
        upperhf(a,b+1)
    else:
        return
    
# Recursion based Code for lower-half pattern printing.
def lowerhlf(a,b):
    if (b>=1):
        print("*"*(a-b) + " "*(2*b-2) + "*"*(a-b))
        lowerhlf(a,b-1)
    else:
        return
    
#Taking Input from the user for pattern size:-
a=int(input("Enter Size of the pattern here! :-"))+1

#Calling Function for pattern printing.
upperhf(a,1)
lowerhlf(a,a-1)