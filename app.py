from Models.DarkGenealogyTree import DarkGenealogyTree
from Models.PlotGraphs import PlotGraphs

tree = DarkGenealogyTree()

PlotGraphs(tree.characters).plot()
