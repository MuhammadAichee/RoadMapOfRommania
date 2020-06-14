try:
    import Queue as Q
except ImportError:
    import queue as Q
import collections

s  =['Arad' ,'Mehadia','Bucharest','Neamt','Craiova','Oradea',
    'Drobeta','Pitesti','Eforie','Rimnicu Vilcea','Fagaras','Sibiu',
    'Giurgiu','Timisoara','Hirsova','Urziceni','Iasi','Vaslui','Lugoj','Zerind']


def DFS(visited,graph,source,destination,level,g_level,flag,cost,parent,p,c,finalcost):
    nayi=[]
    newcost=[]
    newvisited=[]
    nayi1=[]
    if (source not in visited):
        if(destination not in visited):
            visited.append(source)
            parent.append(p)
            finalcost.append(c)
        if(source==destination):
            
            flag=1
            slen=len(visited)
            i=0
            newfinal=[]
            final=visited
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
            newvisited.pop()
            while(len(newvisited)>1 or i>=0 or len(finalparent)>1):
                i=len(finalparent)-1
                if(len(newvisited)==0 or len(finalparent)==0 or i>len(finalparent) or source in nayi ):
                    break
                elif(len(newvisited)>0 and len(finalparent)>0):
                    j=len(newvisited)-1
                    if(newvisited[j]==finalparent[i]):
                        a=newvisited[j]
                        nayi.append(a)
                        while((a!=finalparent[len(finalparent)-1]) or source not in nayi or a not in nayi):
                            if(len(newvisited)==len(finalparent)):
                                break
                            s[finalparent.pop()]
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
            print(s[destination])
            
            
            print("\n")
            exit()
            
            return flag
        if(destination not in visited):
            if(level>g_level):
                flag=0
                return flag
            level=level+1
            a=0
            while(a<20):
                if(source==destination):
                    flag=1
                    exit()
                    return flag
                if(graph[source][a]>0):
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
        if flag==1:
            return
        visited=[]
        parent=[]
        finalcost=[]
        i=i+1
        g_level=g_level+1
    return