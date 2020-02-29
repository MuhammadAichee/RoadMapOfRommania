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
def BFS(s,graph,source,dest):
    # start=0
    cost=0
    if(source==dest):
        print(source)
        return 0
    # print("Starting")
    # print(source)
    # print(dest)
    extra=[]
    parent=[]
    queue =[]
    visited=[]
    visited.append(source)
    queue.append(source)
    parent.append(-1)
    vertex=source    
    while (vertex!= dest and len(queue)>0):
        # print("Source",s[vertex])
        vertex=queue.pop(0)
        visited.append(vertex)
        if(len(extra)>0):
            cost=cost+extra.pop(0)
        a=0
        while a<20:
            if (graph[vertex][a] > 0):
                if(a not in visited and a not in queue):
                    # print(a)
                    # print(visited)
                    queue.append(a)
                    parent.append(vertex)
                    extra.append(graph[vertex][a])
                    if(vertex==dest):
                        break
                     
            a=a+1
    # print(visited)
    # parent.reverse()
    visited.reverse()
    # visited= set(visited)
    # print(visited)
    # print(len(visited))
    # print(len(parent))
    # print
    # i=0
    # while(i<20):
    #     if(i in visited):
    #         print(s[i])
    #     i=i+1
    print("Total Cost",cost)
    while(len(visited)>0):
        print(s[visited.pop()],end=" -> ")    
    print("Total Cost: ",cost)        
i=0
j=0
string=''
source=input("Enter Source: ")
while string!=source:
    string=s[i]
    i=i+1
# print(i-1)
destination=input("Enter Destination: ")    
while string!=destination:
    string=s[j]
    j=j+1
# print(j-1)    
BFS(s,graph,i-1,j-1)
