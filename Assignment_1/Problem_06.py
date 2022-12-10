#QUESTION 06
""" Write a function that takes a positive integer “n” as a parameter and prints the pattern of the type given below for n=7.
Remember that print("*", end="") will not print the newline, and you can print() and can just print a new line.
In the main program, take user input as n and call this function for printing."""

#CODE:
#Taking Input:
n=int(input())

#Buliding Pattern:
for d in range(n):
    for e in range(d+1):
        print("*", end="")
    for g in range(d,n-1):
        print(' ',end="")
    for g in range(d,n-1):
        print(' ',end="")
    for c in range(d+1):
        print("*",end="")
    print("Enter Number for the Pattern Size:")