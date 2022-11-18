from Models.DarkGenealogyTree import DarkGenealogyTree
from Models.PlotGraphs import PlotGraphs
from Utils.dictGraph import dictGraph

graph = dictGraph()
level = {}

visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:        # Creating loop to visit each node
    m = queue.pop(0) 
    print (m) 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        level[neighbour] = level[m] + 1
        queue.append(neighbour)
        
# Driver Code
print("Following is the Breadth-First Search")
level['Bernd Doppler'] = 0
bfs(visited, graph, 'Bernd Doppler')    
print(level)