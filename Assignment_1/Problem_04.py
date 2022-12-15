#QUESTION 06
"""Suppose the velocity of a rocket at a time t is given by:

f(t) = 2000ln[(140000)/(140000 - 2100t)] - 9.8t

Take as input starting time "a" and ending time "b", and find the distance covered by a rocket between time a and b.
For computationally determining the distance, work with time increments (delta) of 0.25 seconds."""

#CODE:
#Importing math module:
import math

#Defining Function for the calculating average value:-
def Avg_val(val1,val2):
    avg_val=0
    avg_val=(val1+val2)/2
    return avg_val

#Calculating velocity:
def Velocity(t):
    if 140000 - 2100*t>0:
        x=math.log((140000)/(140000 - 2100*t))
        vel=2000*(x) - 9.8*t
    
    else:
        print("Type Time in which motion is defined.")
        a=int(input("Starting Time:- "))
        b=int(input("Ending Time:- "))
    return vel

#Defining function to work with time increments of 0.25 seconds to get distance.
def Cal_dis(a,b):
    Tot_dist=0
    no_loops=(b-a)*4
    for i in range(no_loops):
        Tot_dist+=Avg_val(Velocity(a),Velocity(a+0.25))*0.25
        a+=0.25
    return Tot_dist

#Taking Input:
a=int(input("Starting Time:- "))
b=int(input("Ending Time:- "))

#Printing
print("The Total Distance is:-",Cal_dis(a,b))