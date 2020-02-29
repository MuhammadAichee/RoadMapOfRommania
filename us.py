try:
    import Queue as Q
except ImportError:
    import queue as Q
import collections
s  =['Arad' ,'Mehadia','Bucharest','Neamt','Craiova','Oradea',
    'Drobeta','Pitesti','Eforie','Rimnicu Vilcea','Fagaras','Sibiu',
    'Giurgiu','Timisoara','Hirsova','Urziceni','Iasi','Vaslui','Lugoj','Zerind']
graph=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 140, 0, 118, 0, 0, 0, 0, 0, 75,],
[0, 0, 0, 0, 0, 0, 75, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 70, 0,],
[0, 0, 0, 0, 0, 0, 0, 101, 0, 0, 211, 0, 90, 0, 0, 85, 0, 0, 0, 0,],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 87, 0, 0, 0,],
[0, 0, 0, 0, 0, 0, 120, 138, 0, 146, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 151, 0, 0, 0, 0, 0, 0, 0, 71,],
[0, 75, 0, 0, 120, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
[0, 0, 101, 0, 138, 0, 0, 0, 0, 97, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 86, 0, 0, 0, 0, 0,],
[0, 0, 0, 0, 146, 0, 0, 97, 0, 0, 0, 80, 0, 0, 0, 0, 0, 0, 0, 0,],
[0, 0, 211, 0, 0, 0 ,0 ,0, 0, 0, 0, 99, 0 ,0 ,0, 0, 0, 0, 0, 0,],
[140, 0, 0, 0, 0, 151, 0, 0, 0, 80, 99, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0,],
[0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
[118, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 111, 0,],
[0, 0, 0, 0, 0, 0, 0, 0, 86, 0, 0, 0, 0, 0, 0, 98, 0, 0, 0, 0,],
[0, 0, 85, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 98, 0, 0, 142, 0, 0,],
[0, 0, 0, 87, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 92, 0, 0,],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 142, 92, 0, 0, 0,],
[0, 70, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 111, 0 ,0 ,0, 0, 0, 0,],
[75, 0, 0, 0, 0, 71, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
def US(s,graph,source,dest):
    total_cost=0
    if(source==dest):
        print(source)
        return 0
    q=Q.PriorityQueue()
    visited=[]
    visited.append(source)
    q.put((0,source))
    vertex=source
    while (vertex!= dest and q.empty()==0):
        cost, vertex=q.get()
        # if(vertex==dest):
        #     return
        # print("Source",s[vertex])
        # print(s[vertex])
        if(vertex not in visited):
            visited.append(vertex)
        a=0
        while a<20:
            print("Visit", visited)
            if (graph[vertex][a] > 0):
                print("neighbour of source",s[a],s[vertex] )
                print("if ke ander ",graph[vertex][a],s[a])
                if(a not in visited):
                    total_cost=cost+graph[vertex][a]
                    q.put((total_cost,a))
                    # extra.append(graph[vertex][a])
                    # if(vertex==dest):
                    #     break
            print("Total Cost",cost)         
            a=a+1
    # print(visited)
    visited.reverse()
    # i=0
    # while i<20:
    #     # print(i)
    #     if(i in visited):
    #         # print(i)
    #         print(s[i])
    #     i=i+1
    while(len(visited)>0):
        print(s[visited.pop()],end=" -> ")
        # print(s[visited.pop()])
    # print("Visit",visited)
    # i=0
    # while(i<20):
    #     if(i in visited):
    #         print(s[visited[i]])
    #     i=i+1
    # print("Total Cost: ",cost)        

i=0
j=0
string=''
source=input("Enter Source: ")
while string!=source:
    string=s[i]
    i=i+1
print(i-1)
destination=input("Enter Destination: ")    
while string!=destination:
    string=s[j]
    j=j+1
print(j-1)    
newlist=US(s,graph,i-1,j-1)
i=0
print(newlist)

