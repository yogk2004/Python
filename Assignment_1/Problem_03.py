#QUESTION 03
""" A vehicle is to travel on demand. Its initial location is given as x0, y0.
(Assume the first statement in your program as assigning initial values, say x0,y0 = 5.0, 5.0).
Repeatedly take as input the distance the vehicle has to travel. If the input given is 0 or lesser,
the travel ends - assume that at least one positive distance will be given.
The direction in which the vehicle is to travel is determined as follows:
1) If distance is <= 25 it travels north. 
2) If between 26-50 it travels south, between 51 and 75 it travels east
3) If between >= 76 it travels west.

Find the final coordinate of the vehicle, the total distance it has traveled, and the straight line distance between the 
initial location and the final location.(use standard formula for distance between two coordinates; note that this distance 
is not same as total distance traveled)."""

#CODE:
#Taking repeated input until a "negative" or "zero" input is given. Also, calculating total distance at the same time.
Total_dis=0
list_dis_inputs=[]
while True:
    Distance=int(input())
    if Distance>0:
        Total_dis+=Distance
        list_dis_inputs.append(Distance)
    elif Distance <=0:
        break

#Defining intial Coordinates:-(Given in question)
x_coord=5.0
y_coord=5.0

#Now, Defining function to calculate the final coordinates:-
def Final_coord (x_coord,y_coord,list_dis_inputs):
    No_input=len(list_dis_inputs)
    for i in range (No_input):
        if list_dis_inputs[i]<=25:
            y_coord+=list_dis_inputs[i]

        elif list_dis_inputs[i]>=26 and list_dis_inputs[i]<=50:
            y_coord-=list_dis_inputs[i]

        elif list_dis_inputs[i]>=51 and list_dis_inputs[i]<=75:
            x_coord+=list_dis_inputs[i]
        
        else:
            x_coord-=list_dis_inputs[i]

    return x_coord,y_coord

Final_coord1,Final_coord2=Final_coord (x_coord,y_coord,list_dis_inputs)
displacement=((Final_coord1-5)**2+(Final_coord2-5)**2)**(1/2)

#Printing DISTANCE,TOTAL DISTANCE,FINAL COORDINATES:-
print("Final coordinates of the vehicle:-",Final_coord1,Final_coord2)
print("Total distance travelled:-",Total_dis)
print("Straight line distance between the initial location and the final location:-",displacement)