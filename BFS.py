def BFS(s,graph,source,dest):
    cost=0
    if(source==dest):
        print(source)
        return 0
    nayi=[]
    extra=[]
    parent=[]
    queue =[]
    visited=[]
    queue.append((source,-1))
    vertex=source    
    while (vertex!= dest and len(queue)>0):
        vertex,p=queue.pop(0)
        visited.append(vertex)
        parent.append(p)
        if(len(extra)>0):
            cost=cost+extra.pop(0)
        a=0
        while a<20:
            if (graph[vertex][a] > 0):
                if(a not in visited and a not in queue):
                    queue.append((a,vertex))
                    extra.append(graph[vertex][a])
                    if(vertex==dest):
                        break
            a=a+1
    size=len(visited)
    newvisited=[]
    i=0
    while(i<size):
        newvisited.append(visited[i])
        i=i+1
    visited.reverse()
    print("Total Cost: ",cost)
    print("Visited Path:",end=" ")
    while(len(visited)>1):
        print(s[visited.pop()],end=" -> ")
    print(s[dest])
    i=0
    i=len(visited)-1
         
    
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