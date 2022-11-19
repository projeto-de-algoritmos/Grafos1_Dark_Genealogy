from dash import Dash, html
import dash_cytoscape as cyto

from Utils.dictGraph import dictGraph

class Graphs:
  def __init__(self):
    self.reset()
    self.setup_elements()

  def reset(self):
    graph = dictGraph()
    edges = []
    for node in graph.keys():
      sons = graph[node]
      for son in sons:
        if son in list(graph.keys()):
          edges.append((node, son))
    
    self.nodes = graph.keys()
    self.edges = edges

  def setup_elements(self):
    elements = []
    
    for node in self.nodes:
      elements.append({'data': { 'id': node, 'label': node }})
    for edge in self.edges:
      ori, dest = edge
      elements.append({'data': { 'source': ori, 'target': dest }})
  
    self.elements = elements

  def set_nodes(self, nodes):
    graph = dictGraph()
    self.nodes = nodes
    edges = []

    for node in nodes:
      sons = graph[node]
      for son in sons:
        if son in nodes:
          edges.append((node, son))

    self.edges = edges
    self.setup_elements()