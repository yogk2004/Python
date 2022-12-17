pop = [50, 1450, 1400, 1700, 1500, 600, 1200]

#Intial Total number of population:-
Total_Popul_start=0
for i in pop:
    Total_Popul_start+=i

#Function to find total population after every "n" years:-
def Cal_popul(pop,time):
    percentage=2.5
    for j in range (time):
        percentage=2.5-0.1*j
        sum_popul=0
        for i in pop:
            y=0
            New_popul=0
            New_popul=i+(i*percentage)/100
            sum_popul+=New_popul
            pop[y]=New_popul
            y+=1
            percentage-=0.4
    return sum_popul

#Printing Max Population, its year and Current Total Population
time=int(input("Enter Year Number:- "))
if time==0:
    print("The Current Population is:-",Total_Popul_start)
else:
    print("The Current Population is:-",Cal_popul(pop,time))
#Maximum values:-

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
        print("The Years after which the maximum population will be reached:-",max_time)
        print("The value of the maximum population:-",max_popul)