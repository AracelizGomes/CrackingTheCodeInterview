#Depth First Search of a connected graph

from collections import defaultdict

class Graph:
  
  #Constructor
  def __init__(self):
  
    #default dict to store Graph
    self.graph = defaultdict(list)
  
  #function to add edge to graph 
  def addEdge(self, u, v):
    self.graph[u].append(v)
    #print(self.graph)
  
  #function used by DFS 
  def DFSHelper(self, v, visited):
    
    #mark current node as visited and print it 
    visited[v] = True
    print(v)
    
    #recur for all the vertices adjacent to this vertex
    for i in self.graph[v]:
      if visited[i] == False:
        self.DFSHelper(i, visited)
    
  
  #DFS traversal - recursively call DFSUtil 
  def DFS(self, v):
      
    #mark all vertices as not visited
    visited = [False]*(len(self.graph))
      
    #recursively call DFSUtil to print DFS traversal
    self.DFSHelper(v, visited)
      

 #Driver code 
g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,2)
print("DFS starting from vertex 2")
g.DFS(2)
