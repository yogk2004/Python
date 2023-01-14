#Question 2:
"""Write a program that will repeatedly take (for a student) input of this type:
course_no, number_of_credits, and grade_received (eg. CSE101 4 A).
These inputs are for the courses the student has done in the semester. If no input is given (i.e. just a return),
that means no courses are left. From this data, print the transcript for the semester for the student as:

Course_no: grade
Course_no: grade
....

SGPA: n.nn  (two decimal places)

In the transcript, the records should be printed such that they are sorted by the course_no
(hint: when sorting a list of tuples/lists, the default sorting is with the first element of the tuple/list).

The course numbers are an alphanumeric string with capital letters in the start and digits at the end (e.g. CSE101, CSSS21),
credits can be 1, 2 or 4, and grade can be A+(10), A(10), A-(9), B(8), B-(7), C(6), C-(5), D(4), F(2)
(the number in () is their numeric equivalent for SGPA calculation.) The SGPA is computed as
(sum of:  credits*grade/ total_credits). If any input is not valid, print a suitable message
("improper course no", "incorrect credit", or "incorrect grade") and ignore that input."""

#CODE:

#Checking alphanumeric:-
def check_course_no(str1):
    Flag_digit=True
    Flag_char=True
    if str1.isalnum():
        for i in range(len(str1)):
            if str1[i].isnumeric()==True:
                Flag_digit=False
            elif Flag_digit==False:
                if str1[i].isnumeric()==False:
                    print("Invalid 'course_no'!")
                    return False
            elif str1[i].isupper()==False:
                print("Invalid 'course_no'!")
                Flag_char=False
                return False
            elif str1[i].isalpha()==True:
                Flag_char=False    
    else:
        print("Invalid 'course_no'!")
        return False
    if Flag_digit==False and Flag_char==False:
        return True
    else:
        print("Invalid 'course_no'!")
        return False
        
def check_credit(str2):
    if str2!="1" and str2!="2" and str2!="4" and str2!="3":
        print("Invalid 'credit'!")
        return False
        

def check_grade(str3):
    if str3!="A+" and str3!="A" and str3!="A-" and str3!="B" and str3!="B-" and str3!="C" and str3!="C-" and str3!="D" and str3!="F":
        print("Invalid 'grade_received'!")
        return False
    

#Taking input:-
list_input=[]
while True:
    list_input.append(input().split())
    if list_input[-1]==[]:
        list_input.pop()
        break
    elif len(list_input[-1])!=3:
        print("Invalid Input! Please enter 'course_no', 'number_of_credits', and 'grade_received' with a spaces in between them.")
        list_input.pop()
    else:
        A=check_course_no(list_input[-1][0])
        B=check_credit(list_input[-1][1])
        C=check_grade(list_input[-1][2])
        if A==False or B==False or C==False:
            list_input.pop()
            print("Please enter a valid entries of the course with all the 'course no.','credit', and 'grade_received' again.")

#Defining list of 'course_no', 'number of credits' and 'grade received' list differently:-
list_course_no=[]
list_no_of_credits=[]
list_grade_received=[]
for i in list_input:
    list_course_no.append(i[0])
    list_no_of_credits.append(int(i[1]))
    list_grade_received.append(i[2])
#Function for Grading point value:-
def gradVal(str1):
    if str1=="A+":
        return 10
    elif str1=="A":
        return 10
    elif str1=="A-":
        return 9
    elif str1=="B":
        return 8
    elif str1=="B-":
        return 7
    elif str1=="C":
        return 6
    elif str1=="C-":
        return 5
    elif str1=="D":
        return 4
    elif str1=="F":
        return 2

#Calculating SGPA:-
sum_credits=0
sum=0
dict_rel=dict(zip(list_course_no,list_grade_received))
for i in range(len(list_no_of_credits)):
    sum+=list_no_of_credits[i]*gradVal(list_grade_received[i])
    sum_credits+=list_no_of_credits[i]
    result=sum/sum_credits
    list_course_no.sort()
    print_course_no=list_course_no[i]
    print_grad=dict_rel[list_course_no[i]]
    print("----------------------------")
    print(f"{print_course_no}: {print_grad}")
print("----------------------------")
print("SGPA: {r:1.2f}".format(r=result))
print("----------------------------")