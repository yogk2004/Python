#QUESTION 08
"""The current population of the world is combined together into groups that are growing at different rates,
and the population of these groups is given (in millions) in a list.  The population of the first group
(is Africa) is currently growing at 2.5% per year, and each subsequent group is growing at 0.4% lesser
i.e. the next group is growing at 2.1% (note: the growth rate can be negative also). For each group, every year,
the growth rate reduces by 0.1. With this, eventually, the population of the world will peak out and after that start declining.
Write a program that prints:
(i) the current total population of the world,
(ii) the years after which the maximum population will be reached, and the value of the maximum population."""

#CODE:
#Defining function for Required Amount Calculation:-
pop = [50, 1450, 1400, 1700, 1500, 600, 1200]

#Intial Total number of population:-
Total_Popul_start=0
for i in pop:
    Total_Popul_start+=i

#Function to find total population after every "n" years:-
def Cal_popul(pop,time):
    popul_index_no=-1
    sum_popul=0
    for i in pop:
        popul_index_no+=1
        percentage=2.5-0.4*(popul_index_no)
        popul_index_no_2=-1
        for j in range (time):
            New_popul=0
            popul_index_no_2+=1
            percentage=percentage-0.1*popul_index_no_2
            New_popul=i+(i*percentage)/100
            if j==(time-1):
                sum_popul+=New_popul
            i=New_popul
            
    return sum_popul
    
#Max Population Function:-
def Max_func(pop):
    if Cal_popul(pop,1)<Total_Popul_start:
        print("The Years after which the maximum population will be reached:-",0)
        print("The value of the maximum population:-",Total_Popul_start)
    else:
        t1=1
        t2=2
        x=Cal_popul(pop,t1)
        y=Cal_popul(pop,t2)
        if x>y:
            print("The Years after which the maximum population will be reached:-",1,"years")
            print("The value of the maximum population:-",Cal_popul(pop,t1))
        while x<y:
            t1+=1
            t2+=1
            x=Cal_popul(pop,t1)
            y=Cal_popul(pop,t2)
            global max_time
            global max_popul
            max_time=t2
            max_popul=Cal_popul(pop,t2)
            return max_time,max_popul

#Printing Max Population, its year and Current Total Population
time=int(input("Enter Year Number:- "))
#Current Population:-
if time==0:
    print("The Current Population is:-",Total_Popul_start)
else:
    print("The Current Population is:-",Cal_popul(pop,time))
#Maximum values:-
x,y=Max_func(pop)
print("The Years after which the maximum population will be reached:-",x,"years")
print("The value of the maximum population:-",y)