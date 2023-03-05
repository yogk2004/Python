#Question 05:-
"""You are given a list of coordinates (each as a x,y tuple) representing a 2D shape. If the shape has N coordinate,
create a Nx3 matrix with the first column having the x values, 2nd column having the y values,
and the third column being 1 for all. This represents the matrix for the shape.

You have to scale this 2D shape. For scaling, take as input cx and cy (scaling parameters) from the user,
and form a matrix of the type:
---------
|cx 0  0|
|0  cy 0|
|0  0  1|
---------
For scaling the shape, multiply the matrix of the shape with this matrix.
Finally, return the new shape in the form of a list of coordinates - which will be the first two columns of the resultant matrix."""

#CODE:

#Taking input:
list_number_int= list(map(int,input("Enter values of main matrix with a space in between (Not scaling parameters 'cx' or 'cy'):- ").strip().split()))
#Making into prefect list:
list_input=[]
for i in range (0,len(list_number_int),2):
    if i+1!=len(list_number_int):
        list_input.append((list_number_int[i],list_number_int[i+1]))
    else:
        print("Ordered pairs are not competely given! Please run the program again.")

#Making a Matrix:
N=len(list_input)
list_matrix=[]
for i in range (N):
    list_matrix.append([])
for j in range(len(list_input)):
    a,b=list_input[j]
    list_matrix[j].append(a)
    list_matrix[j].append(b)
    list_matrix[j].append(1)
print(list_matrix)

#Making other matrix:
cx=int(input("Enter scaling parameter cx:-"))
cy=int(input("Enter Scaling parameter cy:-"))

list_scaling_matrix=[[cx,0,0],[0,cy,0],[0,0,1]]

#Mutliplying matrix:-
mult_mat_ans=[]
sum=0
for i in range(N):
    mult_mat_ans.append([])
for count in range (N):
    for count2 in range (3):
        for count3 in range (3):
            sum+=list_matrix[count][count3]*list_scaling_matrix[count3][count2]
        mult_mat_ans[count].append(sum)
        sum=0

final_list=[]
a1,a2,a3=(0,0,0)
for i in range(len(mult_mat_ans)):
    [a1,a2,a3]=mult_mat_ans[i]
    final_list.append((a1,a2))
print("")
print("New shape in the form of a list of coordinates:-")
print(final_list)