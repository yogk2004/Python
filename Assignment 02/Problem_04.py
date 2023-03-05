#Question 04:-
"""The goal of this game is for the user (player) to guess the 5 character word in a limited number of chances.

Pick up at least 50 5 character words (e.g. from https://7esl.com/5-letter-words/ ) and save them in a list
or any other structure (you can assign them in a statement, i.e. hard code them).
Select a word at random from this list.

Now prompt the user to input a five character string as his/her guess. After the guess,
the program should show the user the chars from the guess string which are in correct places,
and correct chars in wrong places, by outputting:
--a-d (if a and d were in the input string and are in these two places in the word), other characters present: b  
(if b is present in the word)"""

#CODE:-

#Hard Coding 50 words with 5 letters:
list_words=["Abuse","Adult","Agent","Anger","Apple","Award","Basis","Beach","Birth","Block","Blood","Board","Brain","Bread","Break"]
list_words1=["Brown","Buyer","Cause","Chain","Chair","Chest","Chief","Child","China","Claim","Class","Clock","Coach","Coast","Court"]
list_words2=["Cover","Cream","Crime","Cross","Crowd","Crown","Cycle","Dance","Death","Depth","Doubt","Draft","Drama","Dream","Dress"]
list_words3=["Enemy","Entry","Error","Event","Faith","Fault","Field","Fight","Final","Floor","Focus","Force","Frame","Frank","Front"]
list_words4=["Fruit","Glass","Grant","Grass","Green","Group","Guide","Heart","Henry","Horse","Hotel","House","Image","Index","Input"]
list_words5=["Issue","Japan","Jones","Judge","Knife","Laura","Layer","Level","Lewis","Light","Limit","Lunch","Major","March","Match"]
list_words6=["Model","Money","Month","Motor","Mouth","Music","Night","Noise","North","Novel","Nurse","Offer","Order","Other","Owner"]
list_words7=["Drink","Drive","Earth","Metal","Panel","Paper","Party","Peace","Peter","Phase","Phone","Piece","Pilot","Pitch","Place"]
list_words8=["Plane","Plant","Plate","Point","Pound","Power","Press","Price","Pride","Prize","Proof","Queen","Radio","Range","Ratio"]
list_words9=["Reply","Right","River","Round","Route","Rugby","Scale","Scene","Scope","Score","Sense","Shape","Share","Sheep","Sheet"]
list_words10=["Shift","Shirt","Shock","Sight","Simon","Skill","Sleep","Smile","Smith","Smoke","Sound","South","Space","Speed","Spite"]
list_words11=["Sport","Squad","Staff","Stage","Start","State","Steam","Steel","Stock","Stone","Store","Study","Stuff","Style","Sugar"]
list_words12=["Table","Taste","Terry","Theme","Thing","Title","Total","Touch","Tower","Track","Trade","Train","Trend","Trial","Trust"]
list_words13=["Truth","Uncle","Union","Unity","Value","Video","Visit","Voice","Waste","Watch","Water","While","White","Whole","Woman","World","Youth"]

list_words=list_words+list_words1+list_words2+list_words3+list_words4+list_words5+list_words6+list_words7+list_words8+list_words9+list_words10+list_words11+list_words12+list_words13

#Choosing a word from the list:
import random
word_index=random.randint(0, 211)

word=list_words[word_index]
#Taking input and comparing:

k=0
word=word.lower()
sam_pos_words=[]
dif_pos_words=[]
while k<6:
    word_guess=input()
    while len(word_guess)!=5:
        print("Please give a '5 letter' word.")
        word_guess=input()
    k+=1
    sam_pos_words=[]
    dif_pos_words=[]
    for i in range(5):
        flag=True
        for j in range(5):
            if word_guess[i]==word[j]:
                if i!=j:
                    if flag:
                        dif_pos_words.append((word_guess[i],i,j))
                        flag=False
                else:
                    sam_pos_words.append((word_guess[i],i))
                    break
    for a1,b1,c1 in dif_pos_words:
        for a2,b2 in sam_pos_words:
            if b1==b2 or c1==b2:
                dif_pos_words.remove((a1,b1,c1))
    for a1,b1,c1 in dif_pos_words:
        for a2,b2,c2 in dif_pos_words:
            if (a1,b1,c1) != (a2,b2,c2):
                if c1==c2:
                    dif_pos_words.remove((a2,b2,c2))
    for b in range(5):
        Flag1=True
        for alpha,index in sam_pos_words:
            if index==b:
                Flag1=False
                print(alpha,end="")
                break
        if Flag1==True:
            print("-",end="")
    print("")
    if len(dif_pos_words)!=0:
        print("Other words that are in the word but are at wrong postions:-")
    bool=True
    for i,j,k in dif_pos_words:
        if bool==False:
            print(",",end="")
        bool=False
        print(i,end="")
    print("")