import BFS
import UCS
import IDDFS
import Best
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


i=0
j=0
string=''
source=input("Enter Source: ")
try:
    while string!=source:
        string=s[i]
        i=i+1
except:
    print("No such place found") 
    exit(1)
    
string=''    
destination=input("Enter Destination: ")    
try:
    while string!=destination:
        string=s[j]
        j=j+1
except:
    print("No such place found") 
    exit(1)       

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
    BFS.BFS(s,graph,i-1,j-1)
    print("\n")
    print("========================UCS========================")
    UCS.UCS(s,graph,i-1,j-1)
    print("\n")
    print("========================GBFS========================")
    Best.Best(s,graph,i-1,j-1)
    print("\n")
    print("========================IDDFS========================")
    IDDFS.IDDFS(visited,graph,i-1,j-1,g_level,flag,parent)
    print("\n")
    print("\n")