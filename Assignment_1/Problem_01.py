#QUESTION 01
""" Write a program to take as input a number between 0 and 99, and print the text equivalent of
the number.
(You may first write a function to print the text for a units digit and test it, and then build the rest)

Bonus Question. Expand the code above to write in text any number lesser than 100 crore. """
#NOTE: THE BONUS QUESTION IS ALSO SOLVED IN THE SOLUTION GIVEN.

#CODE:
#Defining Function for names of numbers:
def unitdigitname(te_digit,un_digit,x):
    if x==0:
        if te_digit!=1:
            if un_digit==1:
                return "one"
            elif un_digit==2:
                return "two"
            elif un_digit==3:
                return "three"
            elif un_digit==4:
                return "four"
            elif un_digit==5:
                return "five"
            elif un_digit==6:
                return "six"
            elif un_digit==7:
                return "seven"
            elif un_digit==8:
                return "eight"
            elif un_digit==9:
                return "nine"
            else:
                return ""
        else:
            return ""
    else:
        if te_digit!=1:
            if un_digit==1:
                return "one "
            elif un_digit==2:
                return "two "
            elif un_digit==3:
                return "three "
            elif un_digit==4:
                return "four "
            elif un_digit==5:
                return "five "
            elif un_digit==6:
                return "six "
            elif un_digit==7:
                return "seven "
            elif un_digit==8:
                return "eight "
            elif un_digit==9:
                return "nine "
            else:
                return ""
        else:
            return ""
def tendigitname(te_digit,un_digit,x):
    if x==0:
        if un_digit==0 and te_digit==1:
            return "ten"
        elif un_digit==1 and te_digit==1:
            return "eleven"
        elif un_digit==2 and te_digit==1:
            return "twelve"
        elif un_digit==3 and te_digit==1:
            return "thirteen"
        elif un_digit==4 and te_digit==1:
            return "fourteen"
        elif un_digit==5 and te_digit==1:
            return "fifteen"
        elif un_digit==6 and te_digit==1:
            return "sixteen"
        elif un_digit==7 and te_digit==1:
            return "seventeen"
        elif un_digit==8 and te_digit==1:
            return "eighteen"
        elif un_digit==9 and te_digit==1:
            return "nineteen"
        elif te_digit==2:
            return "twenty"
        elif te_digit==3:
            return "thirty"
        elif te_digit==4:
            return "forty"
        elif te_digit==5:
            return "fifty"
        elif te_digit==6:
            return "sixty"
        elif te_digit==7:
            return "seventy"
        elif te_digit==8:
            return "eighty"
        elif te_digit==9:
            return "ninety"
        else:
            return ""
    else:
        if un_digit==0 and te_digit==1:
            return "ten "
        elif un_digit==1 and te_digit==1:
            return "eleven "
        elif un_digit==2 and te_digit==1:
            return "twelve "
        elif un_digit==3 and te_digit==1:
            return "thirteen "
        elif un_digit==4 and te_digit==1:
            return "fourteen "
        elif un_digit==5 and te_digit==1:
            return "fifteen "
        elif un_digit==6 and te_digit==1:
            return "sixteen "
        elif un_digit==7 and te_digit==1:
            return "seventeen "
        elif un_digit==8 and te_digit==1:
            return "eighteen "
        elif un_digit==9 and te_digit==1:
            return "nineteen "
        elif te_digit==2:
            return "twenty "
        elif te_digit==3:
            return "thirty "
        elif te_digit==4:
            return "forty "
        elif te_digit==5:
            return "fifty "
        elif te_digit==6:
            return "sixty "
        elif te_digit==7:
            return "seventy "
        elif te_digit==8:
            return "eighty "
        elif te_digit==9:
            return "ninety "
        else:
            return ""
def places_name(list_of_number,no_digits,x):
    if x==0:
        if no_digits==2 and list_of_number[2]!=0:
            return "hundred"
        elif no_digits==3 and (list_of_number[3]!=0 or list_of_number[4]!=0):
            return "thousand"
        elif no_digits==6 and (list_of_number[5]!=0 or list_of_number[6]!=0):
            return "lakh"
        elif no_digits==7 and (list_of_number[7]!=0 or list_of_number[8]!=0):
            return "crore"
        else:
            return ""
    else:
        if no_digits==2 and list_of_number[2]!=0:
            return "hundred "
        elif no_digits==3 and (list_of_number[3]!=0 or list_of_number[4]!=0):
            return "thousand "
        elif no_digits==5 and (list_of_number[5]!=0 or list_of_number[6]!=0):
            return "lakh "
        elif no_digits==7 and (list_of_number[7]!=0 or list_of_number[8]!=0):
            return "crore "
        else:
            return ""

#  MAIN FUNCTION:-
#Taking Input
number=input("Enter any Number less than 100 crore (excluding 100 crore):- ")

#Defining list for digits storage in number
list_of_number=[]
list_of_spacing=[]

#Taking Number at each digit at specific position.
no_digits=len(number)
left_digit=9-no_digits
for i in range (no_digits):
    list_of_number.append(int(number[i]))
list_of_number.reverse()
for i in range (left_digit):
    list_of_number.append("")

#Resolving Spacing Problem:
bool=True
for  i in range(1,no_digits+1):
    if bool==False:
            list_of_spacing.append(0)
    else:
        list_of_spacing.append(1)
    if i !=no_digits:   
        for j in range(i):
            if  list_of_number[j]==0:
                bool=False
            else:
                bool=True
                break
#Special for a case of spacing:
if list_of_number[1]==1 or list_of_number[0]==0:
    a=0
else:
    a=1

#Finding which string should be taken
if no_digits==3:
    number_name=unitdigitname(0,list_of_number[2],1)+places_name(list_of_number,2,list_of_spacing[2])+tendigitname(list_of_number[1],list_of_number[0],a)+unitdigitname(list_of_number[1],list_of_number[0],0)
elif no_digits<=2:
    number_name=tendigitname(list_of_number[1],list_of_number[0],a)+unitdigitname(list_of_number[1],list_of_number[0],0)
elif no_digits>=3 and no_digits<6:
    number_name=tendigitname(list_of_number[4],list_of_number[3],1)+unitdigitname(list_of_number[4],list_of_number[3],1)+places_name(list_of_number,3,list_of_spacing[3])+unitdigitname(0,list_of_number[2],1)+places_name(list_of_number,2,list_of_spacing[2])+tendigitname(list_of_number[1],list_of_number[0],a)+unitdigitname(list_of_number[1],list_of_number[0],0)
elif no_digits>=6 and no_digits<8:
    number_name=tendigitname(list_of_number[6],list_of_number[5],1)+unitdigitname(list_of_number[6],list_of_number[5],1)+places_name(list_of_number,5,list_of_spacing[5])+tendigitname(list_of_number[4],list_of_number[3],1)+unitdigitname(list_of_number[4],list_of_number[3],1)+places_name(list_of_number,3,list_of_spacing[3])+unitdigitname(0,list_of_number[2],1)+places_name(list_of_number,2,list_of_spacing[2])+tendigitname(list_of_number[1],list_of_number[0],a)+unitdigitname(list_of_number[1],list_of_number[0],0)
else:  
    number_name=tendigitname(list_of_number[8],list_of_number[7],1)+unitdigitname(list_of_number[8],list_of_number[7],1)+places_name(list_of_number,7,list_of_spacing[7])+tendigitname(list_of_number[6],list_of_number[5],1)+unitdigitname(list_of_number[6],list_of_number[5],1)+places_name(list_of_number,5,list_of_spacing[5])+tendigitname(list_of_number[4],list_of_number[3],1)+unitdigitname(list_of_number[4],list_of_number[3],1)+places_name(list_of_number,3,list_of_spacing[3])+unitdigitname(0,list_of_number[2],1)+places_name(list_of_number,2,list_of_spacing[2])+tendigitname(list_of_number[1],list_of_number[0],a)+unitdigitname(list_of_number[1],list_of_number[0],0)
#Printing the string of the Number
print(number_name)
#NOTE: THE BONUS QUESTION IS ALSO SOLVED ABOVE AND THE SPACES PRECISION BETWEEN THE NAME STRINGS AND ALSO NOT PROVIDING IN THE END AT THE STRING IS TAKEN INTO ACCOUNT.