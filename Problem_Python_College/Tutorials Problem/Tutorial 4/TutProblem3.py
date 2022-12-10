operation=input()
a=int(input())
b=int(input())

def funcX(operation,a,b):
    if operation == "add":
        return a+b
    elif operation=="sub":
        return a-b
    elif operation=="mul":
        return a*b
    else:
        return a/b
print(funcX(operation,a,b))