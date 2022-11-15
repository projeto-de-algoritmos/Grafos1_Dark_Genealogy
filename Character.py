class Character:
  def __init__(self, name, sons):
    self.name = name
    relatives = []
    for son in sons:
      relatives.append(son)
    self.sons = relatives