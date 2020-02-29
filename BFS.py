try:
    import Queue as Q
except ImportError:
    import queue as Q
import collections

# import queue
# class Vertex:
#     def __init__(self, node):
#         self.id = node
#         self.adjacent = {}

#     def __str__(self):
#         return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

#     def add_neighbor(self, neighbor, weight=0):
#         self.adjacent[neighbor] = weight

#     def get_connections(self):
#         return self.adjacent.keys()  

#     def get_id(self):
#         return self.id

#     def get_weight(self, neighbor):
#         return self.adjacent[neighbor]

# class Graph:
#     def __init__(self):
#         self.vert_dict = {}
#         self.num_vertices = 0

#     def __iter__(self):
#         return iter(self.vert_dict.values())

#     def add_vertex(self, node):
#         self.num_vertices = self.num_vertices + 1
#         new_vertex = Vertex(node)
#         self.vert_dict[node] = new_vertex
#         return new_vertex

#     def get_vertex(self, n):
#         if n in self.vert_dict:
#             return self.vert_dict[n]
#         else:
#             return None

#     def add_edge(self, frm, to, cost = 0):
#         if frm not in self.vert_dict:
#             self.add_vertex(frm)
#         if to not in self.vert_dict:
#             self.add_vertex(to)

#         self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
#         self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

#     def get_vertices(self):
#         return self.vert_dict.keys()

# def BFS(graph,source,dest):
#     # print(source)
#     # for putting in queue
#     track=[]
#     # PriorityQueue(maxsize=100)
#     discovered =[] #for visited unvisted
#     q=queue.Queue(100)
#     # print(source)
#     q.put(source)
#     while(q.empty()==False):
#         # print(q.queue[0])
#         current=q.queue[0]
#         q.get()
#         if(current==dest):
#             cost=-1
        
#             print("Least cost from ",source, "to ", dest, "is ",cost)
#             # print()
#     for v in graph:
#         for w in v.get_connections():
#             if(v.get_id() not in q):
#                 discovered.append(v.get_id())
#                 q.put(v.get_id())
#                 track[v.get_id()]=current
     


# if __name__ == '__main__':

#     g = Graph()

#     g.add_vertex(0)
#     g.add_vertex(1)
#     g.add_vertex(2)
#     g.add_vertex(3)
#     g.add_vertex(4)
#     g.add_vertex(5)

#     g.add_edge(0, 1, 7)  
#     g.add_edge(0, 2, 9)
#     # g.add_edge(0, 'f', 14)
#     g.add_edge(1, 2, 10)
#     g.add_edge(1, 3, 15)
#     g.add_edge(2, 3, 11)
#     # g.add_edge(2, 'f', 2)
#     g.add_edge(3, 4, 6)
#     # g.add_edge(4, 'f', 9)

#     for v in g:
#         for w in v.get_connections():
#             vid = v.get_id()
#             wid = w.get_id()
#             print ('( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w)))

#     for v in g:
#         print ('g.vert_dict[%s]=%s' %(v.get_id(), g.vert_dict[v.get_id()]))

#     BFS(g,1,2)
i=0
q=Q.PriorityQueue()
q.put(i+1)
q.put(i+1)
q.put(i+1)
print("Ahsan")    
while not q.empty():
    try:
        q.get(False)
    except Empty:
        continue
    q.task_done()
print(q.empty())    
print("Ahsan")    