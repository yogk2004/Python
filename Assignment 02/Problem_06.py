#Question 06:-
"""For IP course, the performance in different elements of the class for students is given in a file (IPmarks.txt):-
one line per student as comma separated values:

Roll_no,  m1, m2, m3,...

Roll_no is a string, while m1, m2, … are integer marks the student got in assessment 1, 2,....

Separately, the weight of each of the assessments is given as a list of tuples
(you can hard code this in your program - assume that correct number of items is provided): 

wts = [(10, 5), (20, 5), (100, 15), (40, 10),...]

Where the first item is the maximum marks of the assessment, and the second is the weight in % this assessment
carries in the final evaluation (the sum of weights should be 100). In the above, assessment 1 (say, a quiz)
has maximum marks of 10 and its weight in the final total is 5%; assessment 3 has max marks of 100, and its weight is 15).
For each student, compute the weighted sum of marks normalized to 100.
(For weighted sum, assessment 1 marks can be normalized to 5, assessment 3 to 15,...),
and the grade, and write it in a file (IPgrades.txt) as:-

Roll_no, total_marks, grade

For grading, assume that A is above 80%, A- from 70, B from 60, B- from 50, C from 40, C- from 35, D from 30, and below 30 is F."""

#CODE:-

"""### NOTE:- The below code input should satisfy these conditions:-
    1) The sum of the weight in ''wts list'' should be equal to '100' only!!
    2) No. of terms in ''wts'' should be equal to ''no. of assignment'' marks written in the input file!!"""

#Opening the input file:
list_data_old=[]
list_data=[]
count=-1
f=open("IPmarks.txt",'rt')
for line in f:
    a=line.split()
    list_data_old.append(a)
f.close()

for i in list_data_old:
        list_data.append([])
        count+=1
        for j in range(len(i)):
            if j!=0:
                if i[j][-1]==",":
                    list_data[count].append(int(i[j][:-1]))
                else:
                    list_data[count].append(int(i[j]))
            else:
                list_data[count].append(i[j])

#Defining the the weight of each of the assessments:
#wts list ""1 entry""-->""Total marks obtained"", ""2 entry""-->""weight of the assignment!""
wts=[(10, 5), (20, 5), (100, 15), (40, 10), (80, 20), (20, 5), (10, 5), (50, 15), (50, 15), (10, 5)]

#Calculating important parameters:-
#Total Marks Obtained:-
weight_list=[]
total_marks=[]
count_assign=0
max_marks=0
for a,b in wts:
    total_marks.append(a)
    weight_list.append(b)
    max_marks+=a
    count_assign+=1

stud_roll=[]
obt_marks=[]
marks_obtained=[]
count=-1
for i in list_data:
    stud_roll.append(i[0])
    obt_marks.append([])
    count+=1
    a=0
    for j in range(count_assign):
        obt_marks[count].append(int(i[j+1]))
        a+=(i[j+1])
    marks_obtained.append(a)

with open("IPgrades.txt",mode="w+") as my_file:
    my_file.write("")
my_file.close()
for i in range(count+1):
    grade_value=0
    for j in range (count_assign):
        grade_value+=(obt_marks[i][j]/total_marks[j])*weight_list[j]

    if grade_value>80:
        grade="A"
    elif grade_value>70:
        grade="A-"
    elif grade_value>60:
        grade="B"
    elif grade_value>50:
        grade="B-"
    elif grade_value>40:
        grade="C"
    elif grade_value>35:
        grade="C-"
    elif grade_value>30:
        grade="D"
    else:
        grade="F"
    
    with open("IPgrades.txt",mode="a") as my_file:
        my_file.write(stud_roll[i]+" Weighted sum of marks normalized to 100:-"+str(grade_value)+", Grade:- '"+grade+"'."+"\n")
        my_file.close()
        print(stud_roll[i]+" Weighted sum of marks normalized to 100:-"+str(grade_value)+", Grade:- '"+grade+"'")
        print("")