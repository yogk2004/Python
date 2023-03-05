#Question 08:-
'''Given a text file (pages.txt) which has lines of the form:-

URLnn, init_importance: text containing some URLnn. 

Each line represents a page with the first URLnn being its URL and init_importance is a number between 0 and 1.0,
which gives the initial importance of this page. The URLnn in the rest of the line refers to the URL links to other
pages that this page contains.(To simplify, instead of giving a full path, we are using URLnn, and instead of having
separate files for each page, we are giving the text of a page as a line in the file). Example:

URL00, 0.5: This is page zero, and has references to URL01, URL09, and also to URL08. It may have repeated references - so there are two references to URL09.
URL02, 0.6: This is another page (page is represented as a line in this). This has reference to URL05, URL04, and URL00
....

Pages are ranked according to their overall importance. Let the total number of unique links in a page i be links[i]
(i.e. these many unique pages this page refers to). The overall importance of a page i is sum over all the pages (j)
which have a link to page i of: init_importance[j]/ links[j]
(i.e. all the pages to which the page j has a link are distributed the importance of this page equally)

Your program has to find the highest ranking N pages (N can be set in a variable or taken as input) for a given input file. 

It seems natural to create a dictionary with page URL as the index, and having its init_importance, overall importance,
the set of URLs it accesses, etc in it. 

Note. This simplified version has only one round of computation for the overall importance from the initi_importance.
The ranking algorithm actually takes the current importance (starting with init_importance, which is often set to 1)
and then updates the importance repeatedly till the changes are very small. If you want, you can extend your program
to implement this.'''

#CODE:-

def uniq_ele(list1):
    list_rep=[]
    for num1 in range(len(list1)):
        for num2 in range(len(list1)):
            if list1[num1]==list1[num2] and num1<num2:
                list_rep.append(list1[num1])
    my_set=set(list1)
    for num3 in list_rep:
        if num3 in my_set:
            my_set.remove(num3)
    return len(my_set)     

list_data=[]
with open("pages.txt", "r") as myfile:
    for line in myfile:
        list_data.append(line.split())
list_key=[]
list_imp=[]
list_link=[]
count=-1
for i in list_data:
    count+=1
    list_link.append([])
    list_key.append(i[0].replace(",",""))
    list_imp.append(i[1].replace(":",""))
    for j in i[2:-1]:
        j=j.replace(",","")
        list_link[count].append(j)
    list_link[count].append(i[-1].replace(".",""))

list_answer=[]
for i in list_key:
    sum=0
    for j in range(len(list_link)):
        if i in list_link[j]:
            b=float(list_imp[j])
            list2=list_link[j]
            a=uniq_ele(list2)
            sum+=b/a
    list_answer.append(sum)

N=int(input("Enter value of N (First N highest ranking pages):- "))
dict1=dict(zip(list_key,list_answer))

for i in range (N):
    max_value = max(zip(dict1.values(), dict1.keys()))[1]
    print(max_value)
    del dict1[max_value]