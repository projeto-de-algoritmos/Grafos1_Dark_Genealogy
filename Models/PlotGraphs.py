from Models.Character import Character
from dash import Dash, html
import dash_cytoscape as cyto

class PlotGraphs:
  def __init__(self, graphs):
    self.edges = []
    self.nodes = [] 
    for node in graphs:
      if not (node.name in self.nodes):
        self.nodes.append(node.name)
        # print(f"Coloquei o {node.name}")
        # print("-----------------------")
        # print("Olhando os filhos...")
      for son in node.sons:
        if not (son in self.nodes):
          self.nodes.append(son)
          # print(f"Coloquei o filho {son}")
        self.edges.append((node.name, son))
        # print(f"Coloquei a aresta {(node.name, son)}")
  def plot(self):
    elements = []
    for node in self.nodes:
      elements.append({'data': { 'id': node, 'label': node }})
    for edge in self.edges:
      ori, dest = edge
      elements.append({'data': { 'source': ori, 'target': dest }})
    app = Dash(__name__)
    app.layout = html.Div([
        html.P("Dash Cytoscape:"),

        cyto.Cytoscape(
            id='cytoscape',
            elements=elements,
            layout={'name': 'breadthfirst'},
            style={'width': '100%', 'height': '720px'}
        )
    ])


    app.run_server(debug=True)
    ...