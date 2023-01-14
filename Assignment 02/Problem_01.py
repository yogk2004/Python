#QUESTION 01
""" The canteen in the Institute maintains has a table of prices of items, like:
Samosa: 15
Idli: 30
Maggie: 50
Dosa: 70

For the program you have to write, set the menu in your program by this statement (feel free to add more items).
menu = [("Samosa", 15), ("Idli", 30), ("Maggie", 50), ("Dosa", 70), ("Tea", 10), ("Coffee", 20), ("Sandwich", 35), ("ColdDrink", 25)]

Write a program to take a user's order on a terminal and compute the bill. First show the menu by printing the menu.
For ordering an item, the user inputs the item number and the quantity desired (e.g. an input can be: 3 1 followed by 1 5 ).
The program should prompt the user to order more, till he/she hits return (without any numbers) - which is the end of the order.
Print a bill for this order in the form (for the input example above):

Maggie, 1, Rs 50
Samosa, 5, Rs 75

TOTAL, 6 items, Rs 125 """

#CODE:

#Defining menu as a list:-
menu_items = [("Samosa",15),("Idli",30),("Maggie",50),("Dosa",70),("Tea",10),("Coffee",20),("Sandwich",35),("ColdDrink",25)]

#Printing Menu:-
print("")
print("MENU:-")
print("--------------------------")
print("|S.No.| Item Name | Cost |")
print("|-----|-----------|------|")
print("|  1  | Samosa    |  15  |")
print("|  2  | Idli      |  30  |")
print("|  3  | Maggie    |  50  |")
print("|  4  | Dosa      |  70  |")
print("|  5  | Tea       |  10  |")
print("|  6  | Coffee    |  20  |")
print("|  7  | Sandwich  |  35  |")
print("|  8  | ColdDrink |  25  |")
print("--------------------------")

#Working on inputs by the user:-

#Taking input from the user:-
list_input=[]
while True:
    list_input.append(input().split())
    if list_input[-1]==[]:
        list_input.pop()
        break
    elif int(list_input[-1][0])>8 and len(list_input[-1])==2:
        print("Invalid Item number! Please type a valid item number.")
        list_input.pop()
    elif int(list_input[-1][0])>8 and len(list_input[-1])!=2:
        print("Invalid Item number and item quantity entered! Please type a valid item number and item quantity")
        list_input.pop()
    elif len(list_input[-1])!=2:
        print("No item quantity is entered! Please type item quantity with item number again")
        list_input.pop()


#Separating valuable values from inputs:-
list_itemnum=[]
list_num=[]
for i in list_input:
    list_itemnum.append(int(i[0]))
    list_num.append(int(i[1]))

#Removing Repeated inputs:-
list_itemnumfinal=[]
list_numfinal=[]
for i in range(len(list_itemnum)):
    if list_itemnum[i] in list_itemnumfinal:
        continue
    else:
        list_itemnumfinal.append(list_itemnum[i])
        list_numfinal.append(list_num[i])
        for j in range(len(list_itemnum)):
            if j>i:
                if list_itemnum[i]==list_itemnum[j]:
                    list_numfinal[-1]=list_numfinal[-1]+list_num[j]

#Printing Bill:
print("Bill:-")
print("--------------------------")
print_itemName=""
print_amount=0
amount_total=0
total_item=0
for i in range(len(list_itemnumfinal)):
    print_itemName=menu_items[list_itemnumfinal[i]-1][0]
    print_amount=menu_items[list_itemnumfinal[i]-1][1]*list_numfinal[i]
    #printing every element:-
    print(f"{print_itemName}, {list_numfinal[i]}, Rs {print_amount}")
    amount_total+=print_amount
    total_item+=list_numfinal[i]
print("--------------------------")
print(f"TOTAL,{total_item} items, Rs {amount_total}")
print("--------------------------")