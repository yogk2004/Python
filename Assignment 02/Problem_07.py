#Question 07:-
"""Write a program to create your own address book, in which each entry has:
Name, address, phone number, and email address.
In the program, the address book should be a dictionary - the key of the dictionary has to be the name of the person,
while the value has to be another dictionary with address, phone, and email as its keys.
Initially, you can assume that people in your directory have unique names. Then modify the program to handle multiple
persons with same name.(One way to handle this is to keep name as the key, but the value may be a list of dictionaries
- one for each person)

Your Program should provide the following operations: 
------------------------------------------------------------
|(i)  | Insert a new entry,                                |
|(ii) | Delete an entry,                                   |
|(iii)| Find all matching entries given a partial name,    |
|(iv) | Find the entry with a phone number or email, and   |
|(v)  | Exit.                                              |
------------------------------------------------------------
When the program exits, it writes the current dictionary in a file (addrbook.txt)
and when it is started again next time, it reads the existing address book."""

#CODE:

#Defining Functions for above 5 operations:

import json

#Function-1:-
def insert(address_book):
    while True:
        Flag = input("Enter Name (or type 'exit' to quit): ").lower()
        if Flag == "exit":
            
            break
        address = input("Enter address:- ")
        phone = input("Enter phone number:- ")
        email = input("Enter email address:- ")
        if Flag in address_book:
            address_book[Flag].append({'address': address, 'phone': phone, 'email': email})
        else:
            address_book.update({Flag: [{'address': address, 'phone': phone, 'email': email}]})

#Writing into the text file:-
    # Serialize the dictionary to a string
    dict_string = json.dumps(address_book)
    # Open a file for writing
    with open("addrbook.txt", "w") as write_myfile:
        # Write the serialized dictionary string to the file
        write_myfile.write(dict_string)
        write_myfile.close()

    for i in address_book:
        for j in address_book[i]:
            print(i,end=": Address:- ")
            print(j["address"],end=", Phone:- ")
            print(j["phone"],end=", Email:-")
            print(j["email"],end=".")
            print("")

#Function-2:-
def delete_entry(address_book):
    while True:
        del_name=input("Enter Name to delete it's entry or type 'exit':- ").lower()
        if del_name!='exit':
            address_book.pop(del_name)
        else:
            break
    #Updating into th text file:-
    # Serialize the dictionary to a string
    dict_string = json.dumps(address_book)
    # Open a file for writing
    with open("addrbook.txt", "w") as write_myfile:
        # Write the serialized dictionary string to the file
        write_myfile.write(dict_string)
        write_myfile.close()

    for i in address_book:
        for j in address_book[i]:
            print(i,end=": Address:- ")
            print(j["address"],end=", Phone:- ")
            print(j["phone"],end=", Email:-")
            print(j["email"],end=".")
            print("")

#Function-3:-
def Find_byname(address_book):
    while True:
        find_value=input("Enter partial name to find all related entires or type 'exit' to exit:- ").lower()
        list_sim=[]
        if find_value!='exit':
            list_keys=address_book.keys()
            n=len(find_value)
            for i in list_keys:
                if i[:n]==find_value.lower():
                    list_sim.append(i)
            if len(list_sim)>=1:
                for i in list_sim:
                    for j in address_book[i]:
                        print(i,end=": Address:- ")
                        print(j["address"],end=", Phone:- ")
                        print(j["phone"],end=", Email:-")
                        print(j["email"],end=".")
                        print("")
            else:
                print("No Match!")
            list_sim=[]
        else:
            break

#Function-4:-
def Find_bynum_email(address_book):
    while True:
        print("-------------------------------")
        print("|(1.)|Find by the Phone Number|")
        print("|(2.)|Find by the Email       |")
        print("|(3.)|Exit                    |")
        print("-------------------------------")
        option2=input("Write the option:- ")
        if option2=="1":
            Flag=True
            phone_search=int(input("Enter Phone Number or type 'Exit' to exit:- "))
            for i in address_book:
                for j in address_book[i]:
                        if int(j["phone"])==phone_search and phone_search!='Exit':
                            Flag=False
                            print(i,end=": Address:- ")
                            print(j["address"],end=", Phone:- ")
                            print(j["phone"],end=", Email:-")
                            print(j["email"],end=".")
                            print("")
                        elif phone_search=='Exit':
                            break
            if Flag:
                print("No Match!")
        elif option2=="2":
            Flag=True
            email_search=input("Enter email or type 'Exit' to exit:- ")
            for i in address_book:
                for j in address_book[i]:
                        if j["email"]==email_search and email_search!='Exit':
                            Flag=False
                            print(i,end=": Address:- ")
                            print(j["address"],end=", Phone:- ")
                            print(j["phone"],end=", Email:-")
                            print(j["email"],end=".")
                            print("")
                        elif email_search=='Exit':
                            break
            if Flag:
                print("No Match!")
        else:
            break
    
#Main Code:

address_book = {}

# Open the file for reading
with open("addrbook.txt", "r") as read_myfile:
    # Read the contents of the file
    dict_string = read_myfile.read()
    # Deserialize the data and store it in a variable
    if dict_string!="":
        address_book = json.loads(dict_string)
        read_myfile.close()

for i in address_book:
    for j in address_book[i]:
        print(i,end=": Address:- ")
        print(j["address"],end=", Phone:- ")
        print(j["phone"],end=", Email:-")
        print(j["email"],end=".")
        print("")

#Calling Function By Choices:-
while True:
    print("-------------------------------------------------------")
    print("|(1.)| Insert a New entry.                            |")
    print("|(2.)| Delete a entry.                                |")
    print("|(3.)| Find all matching entries given a Partial Name.|")
    print("|(4.)| Find the entry with a Phone Number or Email.   |")
    print("|(5.)| Exit.                                          |")
    print("-------------------------------------------------------")
    option_1=input("ENTER YOUR OPTION:- ")

    if option_1=="1":
        insert(address_book)
    elif option_1=="2":
        delete_entry(address_book)
    elif option_1=="3":
        Find_byname(address_book)
    elif option_1=="4":
        Find_bynum_email(address_book)
    else:
        for i in address_book:
            for j in address_book[i]:
                print(i,end=": Address:- ")
                print(j["address"],end=", Phone:- ")
                print(j["phone"],end=", Email:-")
                print(j["email"],end=".")
                print("")
        break