try:
    import Queue as Q
except ImportError:
    import queue as Q
import collections
s  =['Arad' ,'Mehadia','Bucharest','Neamt','Craiova','Oradea',
    'Drobeta','Pitesti','Eforie','Rimnicu Vilcea','Fagaras','Sibiu',
    'Giurgiu','Timisoara','Hirsova','Urziceni','Iasi','Vaslui','Lugoj','Zerind']

hv=[366,241,0,234,160,380,242,100,161,193,176,253,77,329,151,80,226,199,244,374]

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
def Best(s,graph,source,dest):
    total_cost=0
    if(source==dest):
        # print(source)
        return 0
    q=Q.PriorityQueue()
    visited=[]
    # visited.append(source)
    q.put((hv[0],0,source))
    vertex=source
    while (vertex!= dest and q.empty()==0):
        value, cost, vertex=q.get()
        # while not q.empty():
        #     q.get(False)
        #     q.task_done()
        # q.clear()
        # while(q.empty!=0):
        #     q.get()
        # print("Ahsan")
        # print(q.get())    
        # q.queue.clear()
        # print(q.get())
        # print("Cost: ",cost, "hv: ",value,"jaga: ", s[vertex])
        # if(vertex==dest):
        #     return
        # print("Source",s[vertex])
        # print(s[vertex])
        
        if(vertex in visited):
            # print(vertex)
            # print(visited)
            print("Stuck in Loop")
            return
        visited.append(vertex)    
        print(visited)
        # if(vertex not in visited):
        
        a=0
        while a<20:
            # print("Visit", visited)
            if (graph[vertex][a] > 0):
                # print("neighbour of source",s[a],s[vertex] )
                # print("if ke ander ",graph[vertex][a],s[a])
                # if(a not in visited):
                total_cost=cost+graph[vertex][a]
                q.put((hv[a],total_cost,a))
                             
            a=a+1
    visited.reverse()        
    print("Total Cost",cost)
    while(len(visited)>0):
        print(s[visited.pop()],end=" -> ")
    
i=0
j=0
string=''
# source=input("Enter Source: ")
while string!="Drobeta":
    string=s[i]
    i=i+1
# print(i-1)
# destination=input("Enter Destination: ")    
while string!="Iasi":
    string=s[j]
    j=j+1
# print(j-1)    
# print(hv)
Best(s,graph,i-1,j-1)

