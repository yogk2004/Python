list=[]
for i in range(3):
    list.append(int(input()))
def pythagorean (list):
    if list[0]**2==list[1]**2+list[2]**2:
        print("True")
    else:
        print("False")
pythagorean(list)