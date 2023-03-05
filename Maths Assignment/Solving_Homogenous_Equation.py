def rref_cal(matrix):
    col = len(matrix[0])
    rows = len(matrix)
    para = 0
    list_test=[]
    for j in range(rows):
        if para >= col:
            return matrix
        else:
            i = j
            while matrix[i][para] == 0:
                i += 1
                if i == rows:
                    i = j
                    para += 1
                    if para == col:
                        return matrix
                    else:
                        continue
            #Reassigning the values:-
            matrix[i], matrix[j] = matrix[j], matrix[i]
            #Using List Reassigning Property:-
            for x in matrix[j]:
                list_test.append(x / matrix[j][para])
            for num in range(len(list_test)):
                a=list_test[num]
                matrix[j][num]=a
            list_test.clear()

            #Reassigning the matrix rows:-
            for i in range(rows):
                if i != j:
                    for num2 in range(col):
                        list_test.append(matrix[i][num2] - matrix[i][para] * matrix[j][num2])
                    for num in range(len(list_test)):
                        a=list_test[num]
                        matrix[i][num]=a
                    list_test.clear()
            para += 1
    return matrix

def dict_assign_val(matrix_rref):
    col = len(matrix_rref[0])
    rows = len(matrix_rref)
    #Defining variables:-
    dict_var={}
    for i in range(col):
        var_name="X"+str(i)
        dict_var[var_name]="free"

    #Taking values of free variable :-
    list_eq=[0]*col
    list_zero=[]
    for i in range(rows):
        if 1 in matrix_rref[i]:
            pivot_index=matrix_rref[i].index(1)
        Flag=True
        for j in range (col):
            if j!=pivot_index and matrix_rref[i][j]!=0:
                list_eq[j]=matrix_rref[i][j]
                Flag=False
        if Flag==False:
            var_name="X"+str(pivot_index)
            dict_var[var_name]=list_eq
            list_eq=[0]*col
        elif 1 in matrix_rref[i]:
            var_name="X"+str(pivot_index)
            dict_var[var_name]=0
    return dict_var

def simplify_dic(dict_main):
    list_fixed_key=[]
    list_eq=[]
    for x in dict_main.keys():
        if dict_main[x] == 0:
            list_fixed_key.append(x)
        elif type(dict_main[x]) is list:
            list_eq.append(x)
    
    for key in list_fixed_key:
        for list_com in list_eq:
            temp_val=int(key[1:])
            dict_main[list_com][temp_val]=0
    
    return dict_main

def para_eq(modify_dict,rref):
    list_const=[]
    list_eq=[]
    list_free=[]
    list_keys=[f"X{col}" for col in range(len(rref[0]))]
    print(list_keys,end="")
    print("=",end="")
    for key in modify_dict.keys():
        if type(modify_dict[key]) is str:
            list_free.append(key[1:])
        elif modify_dict[key] == 0:
            list_const.append(key[1:])
        else:   
            list_eq.append(key[1:])

    list1=[0]
    list2=list1*len(rref[0])
    
    Flag=False
    for i in list_free:
        if Flag==True:
            print("+ ",end="")
        for k,val in modify_dict.items():
            if type(val) is list:
                a=int(k[1:])
                b=int(i)
                list2[a]=-(val[b])
            elif type(val) is str:
                c=int(k[1:])
                if c==int(i):
                    list2[c]=1
        print(list2,end="")
        print(f"X{i} ",end="")
        Flag=True
        list1=[0]
        list2=list1*len(rref[0])

    if len(list_free)==0:
        print(list2)


# Matrix input Assignment:-
f=open("Input_matrix.txt",'rt')
matrix_input=[]
count=0
for line in f:
    a=line.split()
    count+=1
    if count>2:
        a=list(map(int,a))
        matrix_input.append(a)
f.close()

rref=rref_cal(matrix_input)

print("Reduced Echelon Form :-")
print(rref)
print("")
dict_main=dict_assign_val(rref)
modify_dict=simplify_dic(dict_main)

print("General Solution in Parametric Vector Form:-")
para_eq(modify_dict,rref)