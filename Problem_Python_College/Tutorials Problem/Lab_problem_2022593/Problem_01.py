import matplotlib.pyplot as mygraph
y=[2, 4, 8, 5]
x=[]
for i in range(1,len(y)+1):
    x.append(i)

mean_val = sum(y)/len(y)
m = []
for i in range(len(y)):
    m.append(mean_val)


mygraph.axhline(y=mean_val, color="Red", linestyle="--")
mygraph.plot(x,y)
mygraph.show()