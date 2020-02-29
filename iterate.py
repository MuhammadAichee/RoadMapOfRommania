class Node:
    name=''
    depthlevel=0
    List=[]
    
    def __init__(self,n):
        self.name=n
    
    def getLevel(self):
        return self.depthlevel
    
    # def addNode(n):
    #     name=n
            
    def addneighbour(self,node):
        self.List.append(node)
         
    def getName(self):
        return self.name
    
    def setLevel(self,value):
        self.depthlevel=value
    
    def getList(self):
        return self.List
    
class Algo:
    targetnode=Node("12")
    isTargetFound=False
    
    def __init__(self,targetNode):
        targetnode=Node(targetNode)
    
    def dfs(self,startNode,depth,targetnode):
        stack=[]
        # nonlocal =Node()
        startNode.setLevel(0)
        stack.append(startNode)
        while(len(stack)>0):
            actualNode=stack.pop()
            print(actualNode.getName()," -> ")
            if(actualNode.getName()==targetnode.getName()):
                print("Node Found")
                isTargetFound=True
            if(actualNode.getLevel()>depth):
                continue
            for(node = Node() : actualNode.getList()):
                node.setLevel(actualNode.getLevel()+1)
                stack.append(node)
    def runDeepningSearch(self,startNode,targetnode):
        depth=0
        while(self.isTargetFound==False):
            self.dfs(startNode,depth,targetnode)
            depth=depth+1
                
    

node1=Node("A")
node2=Node("B")
node3=Node("C")
node4=Node("D")

node1.addneighbour(node2)
node2.addneighbour(node3)
node2.addneighbour(node4)

algo=Algo(node1)
algo.runDeepningSearch(node1,node4)                         
# class Car:
#     name=""
#     def __init__(self , n):
#         self.name=n

# new1=Car        