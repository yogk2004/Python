#list= [map(int, input().split())]
#print(list)

# number of elements
n = int(input("Enter number of elements : "))

# Below line read inputs from user using map() function
a = list(map(str,input("Enter the numbers : ").strip().split()))[:n]

print("List is - ", a)