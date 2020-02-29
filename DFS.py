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
            
            print("Total Cost: ",sum(finalcost))
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
i=0
j=0
string=''
# source=input("Enter Source: ")
while string!="Drobeta":
    string=s[i]
    i=i+1
source=i-1    
# print(i-1)
# destination=input("Enter Destination: ")    
while string!="Iasi":
    string=s[j]
    j=j+1
destination=j-1
IDDFS(visited,graph,source,destination,g_level,flag,parent)    
# DFS(visited,graph,source,destination,level)                
# print(visited,end='    ')
