#BFS stands for Breadth-First Search
#It is a node method for obtainingthe graph's shorest path.
#LEETCODE PROBLEM:-
"""Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1,
find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i
(i.e., there is a directed edge from node i to node graph[i][j]).

Example:-
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
Graph:
0-->1
|   |
\/ \/
2-->3
"""

#Code:
#Input Statement of list into list:-
graph = []
n=int(input("Enter no of Rows:- "))
for i in range (n):
    graph.append([])
    m=int(input("Enter no. of columns in",i,"row:- "))
    for j in range (m):
        graph[i].append(int(input()))

#Defining function:
#Input graph with the index of that number telling that it is connected to which of the number:
def allPathsSourceTarget(graph):

    #Intializing the list for string the required final path:-
    storagePath=[]

    #Defining Another Function:
    #With input of last element and the last list made, we find the next element that is in option and make
    #make for loop for those elements but of it is the last element then is the whole list is stored in the
    #storage path as Nested list:-
    def nextconn (intial_list,lastEle):

        #If we get the last required element (len(graph)-1) element then:
        if lastEle==len(graph)-1:
           storagePath.append(intial_list+[lastEle])
        #If the element has further paths to go forward for and making the for loop case for each element 
        #Nested in the for loop of the previous cases and continuing with the next option in it!
        else:
            for j in graph[lastEle]:
                nextconn (intial_list+[lastEle], j)

    #for Starting  the inside function by giving the intial input!   
    nextconn ([],0)
    #Returning the final path of a particular case!
    return storagePath

#calling a function from the main program.
allPathsSourceTarget(graph)