#Question 07:-
'''Write a program to merge address book of your friend with yours. For this, you can store the
address book as a json or as a list of dictionary items - if both you and your friend agree to the structure,
merging will be easier. '''

#CODE:-
import json

with open("frd_addrbook_bonus.txt", "r") as read_myfile:
    dict_string = read_myfile.read()
    if dict_string!="":
        address_book2 = json.loads(dict_string)
        read_myfile.close()

with open("addrbook.txt", "r") as read_myfile:
    dict_string = read_myfile.read()
    if dict_string!="":
        address_book = json.loads(dict_string)
        read_myfile.close()

for i in address_book2:
    for j in address_book2[i]:
        address = j["address"]
        phone = j["phone"]
        email = j["email"]
        if i in address_book:
            address_book[i].append({'address': address, 'phone': phone, 'email': email})
        else:
            address_book.update({i: [{'address': address, 'phone': phone, 'email': email}]})

print("New dictionary in the addrbook file:-\n{}".format(address_book))

#Writing into the text file:-
dict_string = json.dumps(address_book)
with open("addrbook.txt", "w") as write_myfile:
    write_myfile.write(dict_string)
    write_myfile.close()