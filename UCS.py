try:
    import Queue as Q
except ImportError:
    import queue as Q
import collections

def UCS(s,graph,source,dest):
    nayi=[]
    total_cost=0
    parent=[]
    if(source==dest):
        print(source)
        return 0
    q=Q.PriorityQueue()
    visited=[]
    visited.append(source)
    q.put((0,source,-1))
    vertex=source
    parent.append(-1)
    while (vertex!= dest and q.empty()==0):
        cost, vertex,p=q.get()
        if(vertex not in visited):
            visited.append(vertex)
            parent.append(p)
        a=0
        while a<20:
            if (graph[vertex][a] > 0):
                if(a not in visited):
                    total_cost=cost+graph[vertex][a]
                    q.put((total_cost,a,vertex))
                    
                 
            a=a+1
    print("Total Cost: ",cost)
    size=len(visited)
    newvisited=[]
    i=0
    while(i<size):
        newvisited.append(visited[i])
        i=i+1
    visited.reverse()
    print("Visited Path:",end=" ")
    while(len(visited)>1):
        print(s[visited.pop()],end=" -> ")
    print(s[dest])
    i=len(newvisited)-1
    newvisited.pop()
    while(len(newvisited)>1 or i>=0 or len(parent)>1):
        i=len(parent)-1
        if(len(newvisited)==0 or len(parent)==0 or i>len(parent) or source in nayi ):
            break
        elif(len(newvisited)>0 and len(parent)>0):
            j=len(newvisited)-1
            if(newvisited[j]==parent[i]):
                a=newvisited[j]
                nayi.append(a)
                while((a!=parent[len(parent)-1]) or source not in nayi or a not in nayi):
                    if(len(newvisited)==len(parent)):
                        break
                    s[parent.pop()]
            else:
                q=len(newvisited)-1
                q=newvisited.pop(q)
                
    nayi1=[]
    while(len(nayi)>0):
        if(nayi[len(nayi)-1] not in nayi1):
            nayi1.append(nayi.pop())
        else:
            nayi.pop()            
    print("Actual Path:",end=" ")
    while(len(nayi1)>0):
        a=nayi1.pop(0)
        print(s[a],end=" -> ")
    print(s[dest])


