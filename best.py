try:
    import Queue as Q
except ImportError:
    import queue as Q
import collections

hv=[366,241,0,234,160,380,242,100,161,193,176,253,77,329,151,80,226,199,244,374]

s  =['Arad' ,'Mehadia','Bucharest','Neamt','Craiova','Oradea',
    'Drobeta','Pitesti','Eforie','Rimnicu Vilcea','Fagaras','Sibiu',
    'Giurgiu','Timisoara','Hirsova','Urziceni','Iasi','Vaslui','Lugoj','Zerind']


def Best(s,graph,source,dest):
    total_cost=0
    if(source==dest):
        return 0
    q=Q.PriorityQueue()
    visited=[]
    q.put((hv[0],0,source))
    vertex=source
    while (vertex!= dest and q.empty()==0):
        value, cost, vertex=q.get()
        if(vertex in visited):
            print("Stuck in Loop")
            return
        visited.append(vertex)    
        a=0
        while a<20:
            if (graph[vertex][a] > 0):
                total_cost=cost+graph[vertex][a]
                q.put((hv[a],total_cost,a))
            a=a+1
    visited.reverse()
    print("Total Cost",cost)
    while(len(visited)>1):
        print(s[visited.pop()],end=" -> ")
    print(s[dest])