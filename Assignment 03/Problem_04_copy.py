#Question 04:-
""" Goal is to develop an application for grading in courses at IIIT-Delhi. The application should provide for:-

(i) Creating a course for grading with its name, credits, list of assessments with percentage  weight for each (e.g. [("quiz", 5),
("mid-sem", 15), …], a grading policy as a list percent for different grades (we will assume that only grades are: A, B, C, D,
and F, so this can be [80, 65, 50, 40] (i.e. A above 80, B between 80 and 65, …, F below 40). However, the final cutoff for
each grade will be within +/- 2 of the percent specified (i.e. for A it will be between 78 and 82) - it will be the higher of two
consecutive marks within this range which have the highest difference. (So, if the marks are 81.9, 81.8, 81.7, 81, 80.9, 80.8…,
then the cutoff will be midpoint of 81.7 and 81, which has a largest gap.

(ii) Adding students' marks for all assessments given in a file - these will be rollno followed by marks for each. Once marks
 are given, it should do the grading - apply the policy to determine the grade for each student. 

It should then ask the professor what he wants to do: 1. Generate a summary - which should print the course info (name, credits),
assessments and their weight, cutoffs for different grades, and grading summary (how many As, how many Bs, etc) 2.
Print the grades of all the students in a file as: rollno, total marks, grade (one line for each student). 3. Search for a student
record - given the roll no, show marks in different assessments, total marks, and final grade.

Develop this program and use it for grading the "IP" course. The assessments and the grading policy is given below (in the main
program steps). The main program can be something like (rough sketch):

1.) cname, credits = "IP", 4
2.) assessments = [("labs", 30), ("midsem", 15), ("assignments", 30), ("endsem", 25)] 
3.) policy = [80, 65, 50, 40, 30]
4.) create-IP course (cname, credits, assessments, policy)
5.) Upload-marks data - call a function/method with input as marks.txt
6.) doGrading - call a function/method 
7.) Loop asking for what operation (1, 2, 3); perform the operation till no input given
"""

#CODE:-

class Student:
    def __init__(self):
        self.mrks=[]
        self.d_m={}
        f=open("marks.txt","r")
        x=f.readlines()
        f.seek(0)
        for i in range(len(x)):
            k=f.readline().split(",")
            k[-1]=k[-1].rstrip("\n")
            for j in range(len(k)):
                k[j]=int(k[j])
            self.mrks.append(k)
            self.d_m[int(self.mrks[i][0])]=self.mrks[i][1:]
    def d_mrks(self):
        return self.d_m


class Course(Student):
    def __init__(self,course,credit,assesment,g_policy):
        self.course=course
        self.credit=credit
        self.assesment=assesment
        self.g_policy=g_policy
        Student.__init__(self)
        self.e_d={}
        self.f_c={}
        self.grades={}

    def eval(self):
        for i,j in Student().d_m.items():
            e=0
            for k in range(len(j)):
                e += (self.assesment[k][-1]/100)*j[k]
            self.e_d[i]=e
        return sorted(self.e_d)
        
    def f_ctof(self):
        global mrk
        mrk=[]
        for i in self.e_d.values():
            mrk.append(i)
        for i in range(len(self.g_policy)):
            gr=self.g_policy[i]
            x=[]
            for j in range(len(self.e_d.values())):
                if(mrk[j]>=float(gr)-2.0 and mrk[j]<=float(gr)+2.0):
                    x.append(mrk[j])
            x.sort(reverse=True)
            mn=0
            mdp=0
            for b in range(len(x)-1):
                if(x[b]-x[b+1]>mn):
                    mdp=(x[b]+x[b+1])/2
            self.f_c[self.g_policy[i]]=mdp
        return self.f_c

    def grading(self):
        c_=[]
        for i in self.f_c.values():
            c_.append(i)
        for i,j in self.e_d.items():
            if(j>c_[0]) :self.grades[i]="A"
            elif(j<=c_[0] and j>c_[1]): self.grades[i]="B"
            elif(j<=c_[1] and j>c_[2]): self.grades[i]="C"
            elif(j<=c_[2] and j>c_[3]): self.grades[i]="D"
            else: self.grades[i]="F"
        return self.grades
        
    def summ(self):
        summa = []
        for i in self.grades.values():
            summa.append(i)
        dc = {}
        for i in summa:
            dc[i] = summa.count(i)
        print(dc)
        return

Ip=Course("IP",4,[("labs", 30), ("midsem", 15),("assignments", 30), ("endsem", 25)],[80, 65, 50, 40])
Ip.eval()
Ip.f_ctof()
print("IIITD IP PROGRAM")
print("1) SUMMARY GENERATOR")   
print("2) WRITING GRADES OF ALL STUDENTS")
print("3) SEARCHING RECORD")
print("4) EXIT")
while True:
    ch=int(input())
    if(ch==1): 
            print("Course Name: ", Ip.course)
            print()
            print("Credits: ", Ip.credit)
            print()
            print("Assessment : ", Ip.assesment)
            print()
            print("Course Policy is:", Ip.g_policy)
            print()
            Ip.eval()
            Ip.f_ctof()
            print("Final cutoff :", Ip.f_c)
            print()
            Ip.grading()
            print("SUMMARY")
            Ip.summ()
            print()
    if ch == 2:
        Ip.eval()
        Ip.f_ctof()
        Ip.grading()
        with open("ot.txt","w") as fe:
         wrt=[]
         g_=[]
         for i in Ip.grades.values():
                g_.append(i)
         for i,j in Ip.e_d.items():
                wrt.append([i,j])
         for i in range(len(wrt)):
              wrt[i].append(g_[i])
         for k in wrt:
             k=str(k).strip("]")
             k=k.strip("[")
             fe.write(str(k)+"\n")
    if ch == 3:
        rolln0=int(input("STUDENT ROLLNO:"))
        f=open("marks.txt","r")
        f.seek(0)
        h=f.readlines()
        f.seek(0)
        mk=[]
        dmk={}
        for i in range(len(h)):
            u=f.readline().split(",")
            u[-1]=u[-1].rstrip("\n")
            for j in range(len(u)):
                u[j]=int(u[j])
            mk.append(u)
            dmk[int(mk[i][0])]=mk[i][1:]
        print("ASSESMENT TYPE MARKS")
        for i in dmk:
            try:
                if(i==rolln0):
                    for j in range(len(mk)):
                        print(" ",Ip.assesment[j][0],dmk[rolln0][j-1])
            except:
                pass
        Ip.eval()
        Ip.f_ctof()
        Ip.grading()
        wrt=[]
        g_=[]
        for i in Ip.grades.values():
            g_.append(i)
        for i,j in Ip.e_d.items():
            wrt.append([i,j])
        for i in range(len(wrt)):
            wrt[i].append(g_[i])
        for i in wrt:
            if(i[0]==rolln0):
                print(f"MARKS {i[1]}, FINAL GRADE {i[-1]}")
    if(ch==4):
        break
    