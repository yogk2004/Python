#Question 02
"""A furniture company manufactures dining room tables and chairs. The relevant manufacturing data are given in the table.4

|--------------------|-----------------------|-----------------------|----------------------------------|
|Department          |Labor-Hours per Tables |Labor-Hours per Chairs |Maximum Labor-Hours Available/day |
|--------------------|-----------------------|-----------------------|----------------------------------|
|Assembly            |          8            |           2           |               400                |
|Finishing           |          2            |           1           |               120                |
|Profit per Unit     | $90 for first M units,| $25 for first M units,|                                  |
|                    |    $100 after that    |     $30 after that    |                                  |
|--------------------|-----------------------|-----------------------|----------------------------------|

Write a program to determine how many tables and chairs should be manufactured each day to realize a maximum profit.
Print the number of chairs, tables, and the maximum profit. Initially have M = 10.
Run the program again for M = 0, 20 and see how the output changes.
Keep the code to compute this simple (even if it is inefficient), and you do not have to optimize the code. """

#CODE:
#Defining equations from the statements:

def profit_calculator(x1,x2,M):
    if x1>=0 and x2>=0 and 8*x1+2*x2<=400 and 2*x1+x2<=120:
#Defining Equation for Profit Calculation:
#(90*M+(x-M)*100)+(25*M+(x2-M)*30)=Profit (After Solving equation):
        global profit
        profit=100*x1+30*x2-15*M
        return profit
    else:
        return 0.0

#Function for Finding solution of Two linear equation:-
def Sol_equation(a,b,c,d,e,f):
    list_sol=[]
    if a!=0:
        if a*e!=b*d :
            matrix=[[a,b,c],[0,e-((b*d)/a),f-((c*d)/a)]]
            
            x2=matrix[1][2]/matrix[1][1]
            x1=(c-(b*x2))/matrix[0][0]
            list_sol.append(x1)
            list_sol.append(x2)
            return list_sol
    else:
        if a*e!=b*d :
            x2=c/b
            x1=(f-e*(c/b))/d
            list_sol.append(x1)
            list_sol.append(x2)
            return list_sol

M=int(input())

# Calling function for solving equation
list2=[[1,0,0,0,1,0],[8,2,400,0,1,0],[8,2,400,1,0,0],[8,2,400,2,1,120],[0,1,0,2,1,120],[1,0,0,2,1,120]]
solution_set=[Sol_equation(1,0,0,0,1,0),Sol_equation(8,2,400,0,1,0),Sol_equation(8,2,400,1,0,0),Sol_equation(8,2,400,2,1,120),Sol_equation (0,1,0,2,1,120),Sol_equation(1,0,0,2,1,120)]

# Above all are the possible values of maxima and minima according to linearprogramming concept.
max_profit=0.0
coordinate=0

for i in range (len(solution_set)):
    profit1=profit_calculator(solution_set[i][0],solution_set[i][1],M)
    if max_profit<profit1:
        max_profit=profit1
        coordinate=i

#Printing required Result in required format.
print("Number of Tables:-",int(solution_set[coordinate][0]),end=", ")
print("Number of Chairs:-",int(solution_set[coordinate][0]),end=", ")
print("Maximum Profit:-",max_profit)