from Models.DarkGenealogyTree import DarkGenealogyTree

def dictGraph():
    tree = DarkGenealogyTree()
    graph = {}

    for person in tree.characters:
        graph[person.name] = person.sons

    return graph