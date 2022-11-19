from Utils.dictGraph import dictGraph
from Utils.familyLevel import familyLevel

graph = dictGraph()
level = {}


def bfs(graph, node, comp): #function for BFS
  visited = []
  queue = []

  visited.append(node)
  queue.append(node)

  while queue:        # Creating loop to visit each node
    m = queue.pop(0) 
    #print (m) 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        level[neighbour] = level[m] + 1
        if neighbour == comp:
          return 1
        queue.append(neighbour)
  
  return 0
        
# Driver Code

def buscaParentesco(pessoa1, pessoa2):
  level[pessoa1] = 0
  if bfs(graph, pessoa1, pessoa2) == 1:
    print(pessoa2, ' eh ', familyLevel[level[pessoa2]], ' da ', pessoa1)
    return

  level[pessoa2] = 0
  if bfs(graph, pessoa2, pessoa1) == 1:
    print(pessoa1, ' eh ', familyLevel[level[pessoa1]], ' da ', pessoa2)
    return
  
  print("Não são parentes")

#print("Following is the Breadth-First Search")
#level['Jonas Kahnwald'] = 0
#bfs(visited, graph, 'Jonas Kahnwald'),     
#print(level)
# Bernd Doppler Jonas Kahnwald