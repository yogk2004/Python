#QUESTION 05
""" A person is standing and is looking at a pole in front of him. Given the angle of view to the top
(in degrees-should be between 0 and 90) and the horizontal distance from the person to the base of the pole (in meters),
you have to find the height of the pole and the length of the line from the person to the top of the pole.
 
Your program has to take as input (from the user on the terminal) the angle (in degrees) and another input for distance 
to the base of the pole. Then it computes and prints the height of the pole and the distance to the tip of the pole."""

#CODE:
#Defining Factorial Function:-
def factorial(a):
    fact_value=0
    if a==1 or a==0:
        fact_value=1
    else:
        fact_value=a*(factorial(a-1))
    return fact_value

#Defining Sine(sin) Function:-
def sin(theta):
    theta=(theta*3.14)/180
    sin_value=0
    n=85
    i=1
    while i<n:
        if i%2==1:
            sin_value+=((theta**(2*i-1))/factorial(2*i-1))
        else:
            sin_value-=((theta**(2*i-1))/factorial(2*i-1))
        i=i+1
    return sin_value

#Defining Cosine(cos) Function:-
def cos(theta):
    theta=(theta*3.14)/180
    cos_value=0
    n=85
    i=0
    while i<n:
        if i%2==0:
            cos_value+=(theta**(2*i))/factorial(2*i)
        else:
            cos_value-=(theta**(2*i))/factorial(2*i)
        i=i+1
    return cos_value

#Defining Tangent(tan) Function:-
def tan(theta):
    tan_value=sin(theta)/cos(theta)
    return tan_value

#Taking input and calculating Height of the pole and also, the distance to the tip of the pole from the person.

theta=float(input("Enter angle in degree (0 to 90):-"))
hor_dist=float(input("Enter horizontal distance:-"))
print("Horizontal Height of the pole:-",tan(theta)*hor_dist)
print("Length of the line from the person to the top of the pole:-",hor_dist/cos(theta))