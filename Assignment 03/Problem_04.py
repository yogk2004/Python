class Course:
    def __init__(self,course_name,credits,assessment_data,grading_policy,student_grades):
        self.course_name=course_name
        self.credits=credits
        self.assessment=assessment_data
        self.grading_policy=grading_policy
        self.students_grades=student_grades
    
    #Writing Details into marks.txt file:-
    def write_details(self):
        with open("marks.txt","a+") as myfile:
            myfile.write(f"Course Name: {self.course_name}\n")
            myfile.write(f"Total Credits: {self.credits}\n")
            myfile.write(f"List of Assessments with percentage weight: {self.assessment}\n")
            myfile.write(f"Given Grading Policy: {self.grading_policy}\n")
            #Writing Grades in the file marks.txt
            for i in student_grades:
                myfile.write("\n")
                for j in i:
                    myfile.write(f"{j} ")
        myfile.close()

    def generate_summary(self,final_cutoff,grade_summary):
        bool=True
        with open("marks.txt","r") as myfile:
            for line in myfile:
                if line.split()[0]=="Course":
                    print(line)
                    bool=False
                elif bool==False:
                    print(line)
                elif line.split()[0:3]==["Given","Grading","Policy:"]:
                    print(line)
                    bool=True
            print(f"Final cutoff: {final_cutoff}")
            print(f"Grade Summary: {grade_summary}")

class Student:
    def __init__(self,assessment_data,grading_policy,student_grades):
        self.assessment_data=assessment_data
        self.grading_policy=grading_policy
        self.student_grades=student_grades

    def Cal_Cutoff(self):
        max=0
        A_new=0
        B_new=0
        C_new=0
        D_new=0
        F_new=0
        for i in self.student_grades:
            for j in range (1,len(i)-1):
                if i[j]<self.grading_policy[0]+2 and i[j+1]<self.grading_policy[0]+2 and i[]:
                    if i[j]-i[j+1]>max or i[j+1]-i[j]>max:
                        list
        

while True:
    print("|-----------------------------------------------|")
    print("| 1.) | Creating a course                       |")
    print("| 2.) | Generate Summary                        |")
    print("| 3.) | Printing Grades                         |")
    print("| 4.) | Search Data of a Student by Roll Number |")
    print("| 5.) | To exit the program                     |")
    print("|-----------------------------------------------|")

    input_choice=input("Give your input here:- ")

    if input_choice=="1":
        course_name=input("Enter Course Name:-")
        credits=input("Enter Number of credits:-")
        assessment_data=[]
        student_grades=[]
        while True:
            assessment_temp=input("Enter Assessment with Assessment weight: ")
            if assessment_temp=="":
                break
            assessment_data.append(tuple([assessment_temp.split()[0],int(assessment_temp.split()[1])]))

        grading_policy=list(input("Enter Grading Policy (Only 4 entries allowed): ").split())

        while True:
            grade_temp=list(input(f"Enter Roll no and Marks gained in the assessment out of 100: ").split())
            if grade_temp==[]:
                break
            student_grades.append(grade_temp)

        course_class=Course(course_name,credits,assessment_data,grading_policy,student_grades)
        course_class.write_details()
    else:
        break
"""     elif input_choice=="2":

    elif input_choice=="3":
    
    elif input_choice=="4":

    else:
        break
 """