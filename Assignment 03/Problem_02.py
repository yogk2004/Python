#Question 02 :-
"""For IIIT-D students living off-campus, Suppose records of whenever a student enters or exits the campus are maintained in a data file. A typical data entry will look like this: "Student_Name, Crossing (can be ENTER or EXIT), Gate-number, Time (in 24 hr format)”
If in the record, a student is shown to enter even if he had previously entered the campus,
i.e., two ENTER entries before EXIT, take the first one.
Similarly, there can be two consecutive EXIT entries from the campus for a student - if so, take the last one.
You are given the data for one day (A sample data file can be downloaded from File).
If for a student there is EXIT but there is no ENTRY - it means he/she came the day before; similarly if ENTRY but no EXIT,
it means that the student will leave next day. To avoid special situations, it is best if you first sort this data w.r.t time.
Note: Use of inbuilt libraries like datetime, etc. is not allowed.

Convert this data into a nested dictionary. The keys should be the name and value should be another dictionary containing
a list of gate no, crossing type, time. Use this dictionary to answer the following queries (for querying, you can write
a small loop and ask for a number between 1 and 3 - nothing given can be the end) :-

1) Given a student name (as input), show the record of students moving in/out of campus (as a list of tuples) in the day
(in a output text file), and whether currently present in campus or not.  Take another input for current time as well.
2) Given the start time and the end time (in 24hr format, both inclusive) as input, determine all the students who entered
the campus during this, and all students who exited the campus during this time. Save the result into an output text file,
with the format similar as the input data file.
3) Given the gate number (as input), determine the number of times students have entered the campus through that gate, and
the number of times students have exited the campus from that gate. 
"""

#CODE:-
#Defining Function for First Function:-
def Student_status(dict_data):
# Given a student name (as input), show the record of students moving in/out of campus (as a list of tuples)
# in the day (in a output text file), and whether currently present in campus or not.
# Take another input for current time as well.
    student_name=input("Enter the Student Name:- ").lower()
    current_time=input("Enter the Current Time (Input Format : HH:MM:SS):- ")
    list_print=[]
    with open ("output_func1.txt","w") as output1:
        if student_name not in dict_data:
            print("Student never entered and exited from any of the gate.")
            output1.write("Student never entered and exited from any of the gate.")
        else:
            for i in dict_data[student_name]:
                list_print.append(tuple(i))
            print("")
            print("Record of students moving in/out of campus")
            print("")
            print("(Exit/Enter,Gate Number,Time)")
            print("")
            print(list_print)
            output1.write(f"{list_print} \n")

            for i in range(len(dict_data[student_name])):
                if int("".join(dict_data[student_name][i][2].split(":")))<=int("".join(current_time.split(":"))) and int("".join(dict_data[student_name][i+1][2].split(":")))>int("".join(current_time.split(":"))):
                    if dict_data[student_name][i][0]=="EXIT":
                        print("Student is 'not' in the 'College Premises'.")
                        output1.write("Student is 'not' in the 'College Premises'.")
                    else:
                        output1.write("Student is 'currently present' in the 'College Premises'.")
                        print("Student is 'currently present' in the 'College Premises'.")

                elif int("".join(dict_data[student_name][i][2].split(":")))>int("".join(current_time.split(":"))) and i==0:
                        if dict_data[student_name][i][0]=="EXIT":
                            output1.write("Student is 'currently present' in the 'College Premises'.")
                            print("Student is 'currently present' in the 'College Premises'.")
                        else:
                            print("Student is 'not' in the 'College Premises'.")
                            output1.write("Student is 'not' in the 'College Premises'.")
    output1.close()

#Defining Function for Second Function:-
def determine_entry_exit(dict_data):
# Given the start time and the end time (in 24hr format, both inclusive) as input, determine all the students
# who entered the campus during this, and all students who exited the campus during this time.
# Save the result into an output text file, with the format similar as the input data file.
    intial_time=int("".join(input("Enter the Intial Time:-").split(":")))
    final_time=int("".join(input("Enter the Final Time:-").split(":")))
    with open("output_func2.txt","w") as output2:
        output2.write("TA, Crossing, Gate number, Time\n")
        print("")
        print("TA, Crossing, Gate number, Time")
        for i in dict_data:
            for j in dict_data[i]:
                if int("".join(j[2].split(":")))>=intial_time and int("".join(j[2].split(":")))<=final_time:
                    output2.write(f"{i}, {j[0]}, {j[1]}, {j[2]}\n")
                    print(f"{i}, {j[0]}, {j[1]}, {j[2]}")
    output2.close()

#Defining Function for Third Function:-
def Find_by_GateNumber(dict_data):
# Given the gate number (as input), determine the number of times students have entered the campus through that gate,
# and the number of times students have exited the campus from that gate.
    gate_input=input("Enter Gate Number:- ")
    count_entry=0
    count_exit=0
    for i in dict_data:
        for j in dict_data[i]:
            if j[1]==gate_input:
                if j[0]=="ENTER":
                    count_entry+=1
                else:
                    count_exit+=1
    print("No of Entries from Gate Number", gate_input,"on that Day:-",count_entry)
    print("No of Exits from Gate Number",gate_input,"on that Day:-",count_exit)

#Taking Input :-
dict_data=dict()
with open("sorted_data.txt","r") as mydata:
    for line in mydata:
        list_temp=line.split(", ")
        list_temp[-1]=list_temp[-1][:-1]
        list_temp[0]=list_temp[0].lower()
        if list_temp!=["ta", "Crossing", "Gate number", "Time"]:
            if list_temp[0] not in dict_data:
                dict_data[list_temp[0]]=[list_temp[1:]]
            else:
                list_temp2=dict_data[list_temp[0]].append(list_temp[1:])
mydata.close()

#Making Nested Dictionary:
nested_dict=dict()
for i in dict_data:
    nested_dict[i]=[]
    for j in dict_data[i]:
        nested_dict[i].append({"Crossing":j[0],"Gate number":j[1],"Time":j[2]})

while True:
    print("|--------------------------------------------------------------------------------|")
    print("| 1.) | Showing record by the student name and it's current presence or absence. |")
    print("| 2.) | Showing Entry/Exit Data within a given Time Frame.                       |")
    print("| 3.) | No. of entries and exit from that specified Gate Number provided.        |")
    print("| 4.) | Type Nothing to exit the Program                                         |")
    print("|--------------------------------------------------------------------------------|")
    chooseoption=input("Choose from the above option given :-")
    if chooseoption=="1":
        Student_status(dict_data)
    elif chooseoption=="2":
        determine_entry_exit(dict_data)
    elif chooseoption=="3":
        Find_by_GateNumber(dict_data)
    elif chooseoption=="":
        break
    else:
        print("Give a valid input!")