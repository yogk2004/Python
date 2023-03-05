#Question 03: 
"""Before you graduate, you get the signature from all your friends in your yearbook - which will be stored as a dictionary
for the program. In this dictionary, the keys are the name of other students in the batch;
the value is either 0 (for not signed) or 1 (for signed).
Like you, all other students are also doing the same - and there is a dictionary entry for each.
For creating this dictionary, input is given in a file - if there are N students, then the file contains:

name1:
name2, 1
name3, 0
name4, 1
......

name2:
name1, 0
name3, 0
name4, 0
......

(Like this data is there for all the graduating students).

Write a program to determine who has the most signatures and who has the least
(if there are more than one for max/min - print all)."""

#CODE:
list_data=[]
f=open("Problem_03_input.txt",'rt')
for line in f:
    a=line.split()
    list_data.append(a)
f.close()

#Creating required Dictionary:-
print("Dictionary of the input is as follows:-")
dict_input={}
for i in list_data:
    if len(i)==1:
        dict_input[i[0]]={}
        key_temp=i[0]
    elif len(i)==2:
        dict_input[key_temp][i[0]]=i[1]
print(dict_input)
print("")

#Determing no of candidates:
count_cand=0
for i in list_data:
    if len(i)==1:
        count_cand+=1
    elif len(i)==0:
        break
    else:
        count_cand+=1
list_data.append([])

#Finding out candidates with maximum/minimum no. of signatures:
count_sig_1=0
count_sig_0=0
max_zeros=0
max_ones=0
list_cand_max=[]
list_cand_min=[]
cand_name=""

for i in list_data:
    if len(i)==1:
        cand_name=i[0].replace(':','')
    elif len(i)==2:
        if i[1]=='0':
            count_sig_0+=1
        elif i[1]=='1':
            count_sig_1+=1
    elif len(i)==0:
        if count_sig_0>max_zeros:
            list_cand_min.clear()
            list_cand_min.append(cand_name)
            max_zeros=count_sig_0
        elif count_sig_0==max_zeros:
            list_cand_min.append(cand_name)
        if count_sig_1>max_ones:
            list_cand_max.clear()
            list_cand_max.append(cand_name)
            max_ones=count_sig_1
        elif count_sig_1==max_ones:
            list_cand_max.append(cand_name)
        count_sig_0=0
        count_sig_1=0

#Printing the result:-
print("Student with most signatures:-")
bool=True
for i in list_cand_max:
    if bool==False:
        print(",",end=" ")
    bool=False
    print(i,end="")
print('.')
print("Student with least signatures:-")
bool=True
for j in list_cand_min:
    if bool==False:
        print(",",end=" ")
    bool=False
    print(j,end="")
print(".")