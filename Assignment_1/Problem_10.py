#Question 10
""" Write a program to computationally find a root of a given polynomial in x.
Your program should have a function to compute the value of the polynomial for a given value of x
(you can assign the coefficients in the first few statements and then compute and return the value).
You should have another function that takes as parameters the function to compute the polynomial
and an initial value of x (x0), which is used to find the root.
For computing the root of the polynomial, use the newton-Raphson method (look it up) - it will
start with assuming the initial root as x0, and if the value of the polynomial is not 0 at x0,
determine the slope at x0 to find x1 - the point where the straight line with this slope will intersect the x-axis.
Then use this x1 and repeat the process. Till the value of the polynomial reaches close to 0
(you can assume that if the polynomial is within +/-0.2, it is a root).

Your main program should ask for the value of x0 and then compute the root.
Try with different values of x0 and see what root it finds you will see that starting point can lead to different roots.
As newton Raphson may not converge, or the polynomial may not have a root, after trying for some number iterations (say 100),
your program should print a suitable message and quit.

For the problem, use the polynomial: x**3 - 10.5*x**2 + 34.5*x - 35  (FYI, this one has 3 different roots) """

#CODE:-
#Defining Function for polynomial value at x
def Cal_FuncX(y):
    #Equation Given in question:-
    result=y**3 - 10.5*y**2 + 34.5*y - 35
    return result

#Defining Function for slope value
def diff_result(y):
    #directly writting as equation is fixed in question
    result_diff=3*y**2 - 21*y + 34.5
    return result_diff

#Defining Function for x coordinate of slope line.
def Find_New_x(y):
    y = y - (Cal_FuncX(y)/diff_result(y))
    return y

#Defining Function to print the root of the equation
def print_root(y):
    while Cal_FuncX(y)<=-0.2 or Cal_FuncX(y)>=0.2:
        y=Find_New_x(y)
    print("The approximate root of the equation is:-",y)

#Taking Input:
y=float(input())
print_root(y)