
from Models.Graphs import Graphs
from Utils.dictGraph import dictGraph
from Utils.familyLevel import familyLevel

graph = dictGraph()
level = {}

def bfs(plot_graphs:Graphs, graph, node, comp): #function for BFS
  visited = []
  queue = []

  visited.append(node)
  queue.append(node)

  while queue:        # Creating loop to visit each node
    m = queue.pop(0)

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        level[neighbour] = level[m] + 1
        if neighbour == comp:
          plot_graphs.set_nodes(visited)
          return 1
        queue.append(neighbour)
  
  return 0
        
# Driver Code

def buscaParentesco(pessoa1, pessoa2):
  plot_graphs = Graphs()

  level[pessoa1] = 0
  if bfs(plot_graphs, graph, pessoa1, pessoa2) == 1:
    return {
      'title': f"{pessoa2} é {familyLevel[level[pessoa2]]} de {pessoa1}",
      'elements': plot_graphs.elements
    }

  level[pessoa2] = 0
  if bfs(plot_graphs, graph, pessoa2, pessoa1) == 1:
    return {
      'title': f"{pessoa1} é {familyLevel[level[pessoa1]]} de {pessoa2}",
      'elements': plot_graphs.elements
    }

  plot_graphs.reset()
  return {
    'title': "Não são parentes",
    'elements': plot_graphs.elements
  }

#print("Following is the Breadth-First Search")
#level['Jonas Kahnwald'] = 0
#bfs(visited, graph, 'Jonas Kahnwald'),     
#print(level)
# Bernd Doppler Jonas Kahnwald