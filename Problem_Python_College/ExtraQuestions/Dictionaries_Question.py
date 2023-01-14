#Question:01
#Convert two lists into a dictionary:-
keys=['Ten','Twenty','Thirty']
values=[10,20,30]

#"zip() Function":- This function takes two or more iterables (like list, dict, string), aggregates them in a tuple, and returns it.
dict1=dict(zip(keys,values))

#Iterate the list using a for loop and range() function and adding to dict using update() method.
dict2=dict()
for i in range(len(keys)):
    dict2.update({keys[i]: values[i]}) # {keys[i]: values[i]} is a small dict that is updated in the dict2 that's why curly brackets are used.


#Question:02
#Merge two Python dictionaries into one:-
dict3 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict4 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict5=dict3.copy()
dict5.update(dict4)

dict5 = {**dict3, **dict4} # "*" collects all the positional arguments in a tuple. ; "**"" collects all the keyword arguments in a dictionary.
# one key is neglected because the duplicate values in dictionaries are not allowed.

#Question:03
#Print the value of key ‘history’ from the below dict
sampleDict = {"class": {"student": {"name": "Mike","marks": {"physics": 70,"history": 80}}}}
print_value=sampleDict["class"]["student"]["marks"]["history"]

#Question:04
#Initialize dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
dict6=dict.fromkeys(employees,defaults)
print(dict6)

#Question:05
