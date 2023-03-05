#Question 03 :-
"""For names of the input files - you can hard code it in a list, and then process them one by one. Or you can name the files
as FILE1.txt to FILEn.txt, and take an integer input regarding the number of files and then read them. You need to write out
the output files in this directory itself.

To score an answer file first determine: 

1.) F1 factor = (Unique words/Total words)
2.) F2 factor = (total occurrences the top 5 most occurring words)/Total words
3.) F3 factor = (number of sentences >35 words or < 5 words)/Total sentences
4.) F4 factor = (Frequency of consecutive [comma+full-stop+colon+semicolon]/Total words)
5.) F5 factor = 1 if (Total word count > 750 words), else 0. 

Net score is: 4 + F1*6 + F2*6 -F3 - F4 - F5.

Some clarifications:
The total sentence count needs to be computed after discounting repeated full stops. For example - I am a student of IIIT Delhi… Here, there are a few consecutive full-stops. We will, however, consider this as a single sentence.  And increase the count of consecutive full-stops/ commas/ semi-colons/ colons /hyphens by one regardless of how many full-stops there are (.. is one and ….. is also one, so is .,.,.,).
Consider words of the same spelling but different cases as the same word.

# Extension Problem:

Using the data of unique words and the total words of each submission, calculate the similarity score of each submission with
every other submission, and if the similarity score exceeds 50%, then write the name of the submission file that is being evaluated 
for plagiarism, along with the name of the file with which plagiarism had been detected, and the similarity score between them.

For similarity score computation of File1 with File2, first:
Determine fCW: common words, with the common frequency in both (i.e. minimum of frequency in the two files) 
Use fCW to determine nSW - which is the sum of all the frequencies of common words - to get the total number of same words
Use fCW to get the number of unique words common to both submissions(nSUW).

Similarity score for File1 sim_index (with File2 is):
sim _index = 100% x [(nSW/total words in File1)+(nSUW/total unique words in File 1)]/2
"""

#CODE:-
import random
def param_cal(data):
    #Defining Variables:-
    total_words=0
    total_lines=0
    list_words=[]
    cond_lines=0
    temp_words=0
    word=""
    temp_max=[]
    a=0
    sum=0
    freq_repeat=0
    data=data.strip(" ")

    # Defining Loops to complete a function:-
    for i in data:
        if i.isalpha()==False and Flag==True:
            Flag=False
            total_words+=1
            temp_words+=1
            list_words.append(word.lower())
            word=""
            if i==".":
                total_lines+=1
                if temp_words>35 or temp_words<5:
                    cond_lines+=1
                temp_words=0
        elif i.isalpha():
            Flag=True
            word=word+i
        elif Flag==False and (i=="." or i=="," or i==";" or i==":"):
            freq_repeat+=1
    uniq_words=len(set(list_words))

    # Calculating occurrences of the Top 5 most occurring words:-
    top_words=[]
    list_uniq_words=[]
    for i in list_words:
        if i not in list_uniq_words:
            list_uniq_words.append(i)
    for j in list_uniq_words:
        temp_max.append(list_words.count(j))
    while a<5:
        max=0
        for j in range(len(temp_max)):
            if max<temp_max[j]:
                max=temp_max[j]
                entry=j
        sum+=max
        top_words.append(list_uniq_words[entry])
        temp_max[entry]=0
        a+=1
    return uniq_words,total_words,sum,cond_lines,total_lines,freq_repeat,top_words,list_words


def fCW_cal(list_words):
    unique_words=[]
    list_count=[]
    for i in list_words:
        if i not in unique_words:
            list_count.append(list_words.count(i))
            unique_words.append(i)
    dict_fCW=dict(zip(unique_words,list_count))
    return dict_fCW


def plag_percent_cal(dict_fCW1,dict_fCW2,total_words_1):
    fCW_main=dict()
    sum=0
    for i in dict_fCW1:
        if i in dict_fCW2:
            if dict_fCW1[i]==dict_fCW2[i]:
                fCW_main[i]=dict_fCW1[i]
    for key in fCW_main:
        sum+=fCW_main[key]
    nSW=sum
    nSUW=len(fCW_main.keys())
    
    #Calculating Percentage:-
    sim_index=100*((nSW/total_words_1)+(nSUW/total_words_1))/2
    return sim_index

#Taking input from the student's files:-
file_amt=int(input("Number of Files:-"))
list_file=[]
list_var=[]
for i in range(1,file_amt+1):
    list_file.append(f"FILE{i}.txt")

list_result=[]
list_plag_fCW=[]
list_all_words=[]
with open ("scores.txt","w") as my_write:
    for i in range(file_amt):
        total_lines=0
        with open (list_file[i],"r") as my_output:
            data=my_output.read()
            uniq_words,total_words,sum,cond_lines,total_lines,freq_repeat,top_words,list_words=param_cal(data)
            F1=uniq_words/total_words
            F2=sum/total_words
            F3=cond_lines/total_lines
            F4=freq_repeat/total_words
            F5= 1 if total_words>750 else 0
            list_plag_fCW.append(fCW_cal(list_words))
            list_all_words.append(total_words)
            list_result.append(4+F1*6+F2*6-F3-F4-F5)
            my_write.write(f"{list_file[i]}\n")
            my_write.write(f"scores: {list_result[i]}\n")
            my_write.write(f"Top 5 most occurring words: {top_words[0]},{top_words[1]},{top_words[2]},{top_words[3]},{top_words[4]}\n")
            my_write.write(f"Five randomly selected words from the submission:- {random.choice(list_words)}, {random.choice(list_words)}, {random.choice(list_words)}, {random.choice(list_words)}, {random.choice(list_words)}\n")
    
    with open("plag.txt","w") as my_write2:
        for i in range(len(list_plag_fCW)):
            for j in range(len(list_plag_fCW)):
                if i!=j:
                    percent=plag_percent_cal(list_plag_fCW[i],list_plag_fCW[j],list_all_words[i])
                    if percent>50:
                        my_write2.write(f"FILE{i}.txt FILE{j}.txt {percent}%\n")

my_output.close()
my_write.close()
my_write2.close()