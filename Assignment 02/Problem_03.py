#Question 3: 
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

#Taking input from the file:
File_obj=open("Problem_03_input.txt","rt")

for line in File_obj:
    print(line)