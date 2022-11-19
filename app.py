from dash import Dash, html, dcc, Input, Output
import dash_cytoscape as cyto
from Models.DarkGenealogyTree import DarkGenealogyTree
from Utils.bfs import buscaParentesco
from Models.Graphs import Graphs
from Utils.dictGraph import dictGraph

app = Dash(__name__)

graphs = Graphs()
characters = list(dictGraph().keys())

app.layout = html.Div(
  style={
    'display': 'flex',
    'flex-direction': 'column',
    'flex': '1',
    'justify-content': 'center',
    'align-items': 'center',
  }, 
  children=[
    html.H1(style={
      'text-align': 'center'
    }, 
    children=[
      "Dark Arvore Genealógica"
    ]),
    html.Div(
      style={
        'display': 'flex',
        'width': '100%'
      }, 
      children=[
        cyto.Cytoscape(
          style={
            'flex': '0.7', 
            'width': '50%', 
            'height': '720px',
          },
          id='cytoscape',
          elements=graphs.elements,
          layout={'name': 'cose'},
        ),
        html.Div(
          style={
            'display': 'flex',
            'flex-direction': 'column',
            'flex': '0.3',
            'padding': '20px',
            'justify-content': 'center'
          },
          children=[
            "Pessoa 1:",
            dcc.Dropdown(style={'margin-bottom': '15px'}, options=characters, value='Jonas Kahnwald',id='pessoa1'),
            "Pessoa 2:",
            dcc.Dropdown(options=characters, value='Regina Tiedemann',id='pessoa2'),
            html.H1(style={'text-align': 'center'}, id='grau-parentesco')
          ]),
      ]
    ),
  ]
)


@app.callback(
  Output(component_id='grau-parentesco', component_property='children'),
  Output(component_id='cytoscape', component_property='elements'),
  Input(component_id='pessoa1', component_property='value'),
  Input(component_id='pessoa2', component_property='value')
)

def update_elements(pessoa1, pessoa2):
  if (pessoa1 != None and pessoa2 != None):
    result = buscaParentesco(pessoa1, pessoa2)
    return result['title'], result['elements']

if __name__ == '__main__':
  app.run_server(debug=True)
  





