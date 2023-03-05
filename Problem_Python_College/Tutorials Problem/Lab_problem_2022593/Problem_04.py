import numpy as my_obj

n = int(input())
beta = int(input())
gamma = int(input())
m = int(input())
list1 = []
list2 = []
for i in range(n):
    temp_list = [float(num) for num in input().split()]
    list1.append(temp_list)

for i in range(gamma):
    temp_list = [float(num) for num in input().split()]
    list2.append(temp_list)

val_A, val_B = my_obj.array(list1), my_obj.array(list2)


if beta != gamma:
    print("Dimensions of matrices are not compatible.")
else:
    val_C = (my_obj.dot(val_A, val_B))
    for row in val_C:
        for j in row:
            print(j, end=" ")
        print()