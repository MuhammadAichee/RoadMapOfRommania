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
def BFS(s,graph,source,dest):
    # start=0
    cost=0
    if(source==dest):
        print(source)
        return 0
    nayi=[]
    extra=[]
    parent=[]
    queue =[]
    visited=[]
    # visited.append(source)
    queue.append((source,-1))
    # parent.append(-1)
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
                # print("neighbour of source",s[a],s[vertex] )
                # print("if ke ander ",graph[vertex][a],s[a])
                if(a not in visited and a not in queue):
                    # print(a)
                    # print(visited)
                    queue.append((a,vertex))
                    # parent.append(vertex)
                    extra.append(graph[vertex][a])
                    if(vertex==dest):
                        break
            # print("Cost",cost)         
            a=a+1
    # print(visited)
    # newvisited=visited
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
    # print("i: ",i)
    # print("Starting mein hi pop kardya",newvisited.pop())
    newvisited.pop()
    while(len(newvisited)>1 or i>=0 or len(parent)>1):
        i=len(parent)-1
        if(len(newvisited)==0 or len(parent)==0 or i>len(parent) or source in nayi ):
            break
        elif(len(newvisited)>0 and len(parent)>0):
            j=len(newvisited)-1
            if(newvisited[j]==parent[i]):
                a=newvisited[j]
                # print("newvisited ka last uthate hue: ",a)
                nayi.append(a)
                # size3=len(parent)-1
                while((a!=parent[len(parent)-1]) or source not in nayi or a not in nayi):
                    # print(parent[len(parent)-1])
                    # size1=len(newvisited)
                    # size2=len(parent)
                    # print("before popping size: ",size1,size2)
                    if(len(newvisited)==len(parent)):
                        # print("Ahsan ",len(parent),len(newvisited))
                        break
                    # print("popping for limiting: ",)
                    s[parent.pop()]
                # print("Popping ki statement se pehle: ",a,parent[len(parent)-1])
                # if(a!=parent[len(parent)-1]):    
                #     print("length after popping: ",len(newvisited),len(parent))
            else:
                # parent.pop()
                # print("in loop value of i",i)
                q=len(newvisited)-1
                q=newvisited.pop(q)
                # print("Tyt: ",a,q)
                # print("Hoja")
                # print("popping from newvisited",q)
    # size=len(nayi)-1
    nayi1=[]
    while(len(nayi)>0):
        if(nayi[len(nayi)-1] not in nayi1):
            nayi1.append(nayi.pop())
        else:
            nayi.pop()            
            # i-i-1       
    # print("length: ",len(nayi))
    print("Actual Path:",end=" ")
    while(len(nayi1)>0):
        a=nayi1.pop(0)
        print(s[a],end=" -> ")
    print(s[dest])


#UCS
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
        # if(vertex==dest):
        #     return
        # print("Source",s[vertex])
        # print(s[vertex])
        if(vertex not in visited):
            visited.append(vertex)
            parent.append(p)
        a=0
        while a<20:
            # print("Visit", visited)
            if (graph[vertex][a] > 0):
                # print("neighbour of source",s[a],s[vertex] )
                # print("if ke ander ",graph[vertex][a],s[a])
                if(a not in visited):
                    total_cost=cost+graph[vertex][a]
                    q.put((total_cost,a,vertex))
                    
                 
            a=a+1
        
    # print(visited)
    # newvisited=[]
    # newvisited=visited
    # print(newvisited)
    print("Total Cost: ",cost)
    size=len(visited)
    newvisited=[]
    i=0
    while(i<size):
        newvisited.append(visited[i])
        i=i+1
    visited.reverse()
    # i=0
    # while i<20:
    #     # print(i)
    #     if(i in visited):
    #         # print(i)
    #         print(s[i])
    #     i=i+1
    print("Visited Path:",end=" ")
    while(len(visited)>1):
        print(s[visited.pop()],end=" -> ")
    print(s[dest])
        # print(s[visited.pop()])
    # print("Visit",visited)
    # i=0
    # while(i<20):
    #     if(i in visited):
    #         print(s[visited[i]])
    #     i=i+1
    # print("Total Cost: ",cost)
    i=len(newvisited)-1
    # print("i: ",i)
    # print("Starting mein hi pop kardya",newvisited.pop())
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
                # print("Popping ki statement se pehle: ",a,parent[len(parent)-1])
                # if(a!=parent[len(parent)-1]):    
                #     print("length after popping: ",len(newvisited),len(parent))
            else:
                # parent.pop()
                # print("in loop value of i",i)
                q=len(newvisited)-1
                q=newvisited.pop(q)
                
    nayi1=[]
    while(len(nayi)>0):
        if(nayi[len(nayi)-1] not in nayi1):
            nayi1.append(nayi.pop())
        else:
            nayi.pop()            
            # i-i-1       
    # print("length: ",len(nayi))
    print("Actual Path:",end=" ")
    while(len(nayi1)>0):
        a=nayi1.pop(0)
        print(s[a],end=" -> ")
    print(s[dest])


visited=[]
parent=[]
finalparent=[]
flag=0
final=[]
g_level=0
def DFS(visited,graph,source,destination,level,g_level,flag,cost,parent,p,c,finalcost):
    nayi=[]
    # finalcost=[]
    newcost=[]
    newvisited=[]
    nayi1=[]
    if (source not in visited):
        if(destination not in visited):
            # print(s[source],end=" -> ")
            # print("Level: ",level)    
            visited.append(source)
            parent.append(p)
            finalcost.append(c)
        # print("Source: ",source," Destination: ",destination)
        if(source==destination):
            
            flag=1
            slen=len(visited)
            # print("length: ", slen)
            i=0
            newfinal=[]
            final=visited
            # newfinal=final
            finalparent=parent
            newvisited=visited
            size=len(visited)
            i=0
            while(i<size):
                newfinal.append(visited[i])
                i=i+1
            print("Total Cost: ",sum(finalcost))
            print("Visited Path:",end=" ")
            newfinal.reverse()
            while(len(newfinal)>1):
                print(s[newfinal.pop()],end=" -> ")        
            print(s[destination])
            # while i<7:
            #     final[i]=visited[i]
            #     print("Final: ",final[i],"visited: ",visited[i])
            #     i=i+1
            # newlen=len(newfinal)
            # while(newlen>0):
            #     print(s[newfinal.pop(0)],end=" -> ")
            #     i=i+1
            #     newlen=len(newfinal)
            # print(final)
            # print(finalcost)
            
            # print(finalparent)
            
            newvisited.pop()
            while(len(newvisited)>1 or i>=0 or len(finalparent)>1):
                i=len(finalparent)-1
                if(len(newvisited)==0 or len(finalparent)==0 or i>len(finalparent) or source in nayi ):
                    break
                elif(len(newvisited)>0 and len(finalparent)>0):
                    j=len(newvisited)-1
                    if(newvisited[j]==finalparent[i]):
                        a=newvisited[j]
                        # print("newvisited ka last uthate hue: ",a)
                        nayi.append(a)
                        # size3=len(parent)-1
                        while((a!=finalparent[len(finalparent)-1]) or source not in nayi or a not in nayi):
                            # print(parent[len(parent)-1])
                            # size1=len(newvisited)
                            # size2=len(parent)
                            # print("before popping size: ",size1,size2)
                            if(len(newvisited)==len(finalparent)):
                                # print("Ahsan ",len(parent),len(newvisited))
                                break
                            # print("popping for limiting: ",)
                            s[finalparent.pop()]
                        # print("Popping ki statement se pehle: ",a,parent[len(parent)-1])
                        # if(a!=parent[len(parent)-1]):    
                        #     print("length after popping: ",len(newvisited),len(parent))
                    else:
                        # parent.pop()
                        # print("in loop value of i",i)
                        q=len(newvisited)-1
                        q=newvisited.pop(q)
            nayi1=[]
            while(len(nayi)>0):
                if(nayi[len(nayi)-1] not in nayi1):
                    nayi1.append(nayi.pop())
                else:
                    nayi.pop()            
                    # i-i-1       
            # print("length: ",len(nayi))
            print("Actual Path:",end=" ")
            while(len(nayi1)>0):
                a=nayi1.pop(0)
                print(s[a],end=" -> ")
            print(s[destination])
            
            
            print("\n")
            exit()
            
            # print("Flag: ",flag)
            return flag
        if(destination not in visited):
            # print(visited,end=' =>')
            # print("Ahsan",source,s[source])
            if(level>g_level):
                flag=0
                return flag
            # visited.append(source)
            # finalcost.append(c)
            # parent.append(p)
            level=level+1
            a=0
            while(a<20):
                if(source==destination):
                    flag=1
                    exit()
                    # print("Flag: ",flag)
                    return flag
            # print("a",a)
                if(graph[source][a]>0):
                # print("Ahsan",a)
                    cost=cost+graph[source][a]
                    DFS(visited,graph,a,destination,level,g_level,flag,cost,parent,source,graph[source][a],finalcost)
                
                a=a+1

def IDDFS(visited,graph,source,destination,g_level,flag,parent):
    level=0
    finalcost=[]
    visited=[]
    parent=[]
    i=0
    while True:
        DFS(visited,graph,source,destination,0,g_level,flag,0,parent,-1,0,finalcost)
        # print(flag)
        if flag==1:
            # print("flag: ",flag)
            return
        visited=[]
        parent=[]
        finalcost=[]
        i=i+1
        g_level=g_level+1
    return

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
        # print(visited)
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
    while(len(visited)>1):
        print(s[visited.pop()],end=" -> ")
    print(s[dest])
i=0
j=0
string=''
# source=input("Enter Source: ")
while string!="Drobeta":
    string=s[i]
    i=i+1
string=''    
# destination=input("Enter Destination: ")    
while string!="Iasi":
    string=s[j]
    j=j+1
if(i-1==j-1):
    print("========================BFS========================")        
    print("\n")
    print("Source and Destination is same. Hence, Total Cost is 0")
    print("\n")
    print("========================UCS========================")
    print("\n")
    print("Source and Destination is same. Hence, Total Cost is 0")
    print("\n")
    print("========================UCS========================")
    print("\n")
    print("Source and Destination is same. Hence, Total Cost is 0")
    print("\n")
    print("========================IDDFS========================")
    print("\n")
    print("Source and Destination is same. Hence, Total Cost is 0")    
    print("\n")
else:
    print("========================BFS========================")
    BFS(s,graph,i-1,j-1)
    print("\n")
    print("========================UCS========================")
    UCS(s,graph,i-1,j-1)
    print("\n")
    print("========================GBFS========================")
    Best(s,graph,i-1,j-1)
    print("\n")
    print("========================IDDFS========================")
    IDDFS(visited,graph,i-1,j-1,g_level,flag,parent)
    print("\n")
    print("\n")