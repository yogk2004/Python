a="Hello World"
#Indexing
print(a[0]) #Give the first word "H" of the string
print(a[8]) #Give the "o" as the result as sapce is also count as in the string counting

#Reverse indexing we put negative numbers
print(a[-2]) #print the last second word of the string. Here,"l".

#Slicing
mystring="helloPythonCode"
#Formats of Slicing: [start:stop:step]
#if we wanted all the string starting from a specific.(ending numbered char is not included only)

print(mystring[2:])
print(mystring[:7])#To grab from starting and till some numbered char.
print(mystring[3:7])#To grab the part of string we needed from 3 numbered till 6 numbered char (last not included)

#valid syntax
print(mystring[::])#means from the starting to the end of the string or we can directly print the string itself

#step size
print(mystring[::2])#Here, it means the string we go from the starting to the end with the jup of 2.

#Full usage
print(mystring[2:7:3])

#Doing Indexing in one line without assigning string to variable.
print("Hello World"[7])  #just can write the char position at the side of string from which it should be taken.

print("Hello World"[2:3:5])