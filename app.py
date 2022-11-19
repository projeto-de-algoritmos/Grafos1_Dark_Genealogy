from Models.DarkGenealogyTree import DarkGenealogyTree
from Utils.bfs import buscaParentesco
#from Models.PlotGraphs import PlotGraphs

tree = DarkGenealogyTree()

#PlotGraphs(tree.characters).plot()

print("Pessoa 1: ")
pessoa1 = input()
print("Pessoa 2: ")
pessoa2 = input()

buscaParentesco(pessoa1, pessoa2)
