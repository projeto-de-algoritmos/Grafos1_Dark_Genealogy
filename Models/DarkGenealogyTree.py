from Models.Character import Character

class DarkGenealogyTree:
  def __init__(self):
    characters = []

    # Tannhaus
    characters.append(Character("Heinrich Tannhaus", ["Gustav Tannhaus"]))
    characters.append(Character("Gustav Tannhaus", ["Leopold Tannhaus"]))
    characters.append(Character("Leopold Tannhaus", ["H.G Tannhaus"]))
    characters.append(Character("H.G Tannhaus", []))

    # Doppler
    characters.append(Character("Bernd Doppler", ["Helge Doppler", "Anatol Veliev", "Regina Tiedemann"]))
    characters.append(Character("Greta Doppler", ["Helge Doppler", "Anatol Veliev"]))
    characters.append(Character("Helge Doppler", ["Peter Doppler"]))
    characters.append(Character("Peter Doppler", ["Elisabeth Doppler", "Franziska Doppler"]))
    characters.append(Character("Charlotte Doppler", ["Elisabeth Doppler", "Franziska Doppler"]))
    characters.append(Character("Elisabeth Doppler", ["Charlotte Doppler"]))
    characters.append(Character("Franziska Doppler", []))

    # Tiedemann
    characters.append(Character("Egon Tiedemann", ["Claudia Tiedemann", "Silja"]))
    characters.append(Character("Doris Tiedemann", ["Claudia Tiedemann"]))
    characters.append(Character("Claudia Tiedemann", ["Regina Tiedemann"]))
    characters.append(Character("Regina Tiedemann", ["Bartosz Tiedemann"]))
    characters.append(Character("Aleksander Tiedemann", ["Bartosz Tiedemann"]))
    characters.append(Character("Bartosz Tiedemann", ["Noah", "Agnes Nielsen"]))

    # Kahnwald
    characters.append(Character("Jonas Kahnwald", []))
    characters.append(Character("Hannah Kahnwald", ["Jonas Kahnwald", "Silja"]))
    characters.append(Character("Daniel Kahnwald", ["Ines Kahnwald"]))
    characters.append(Character("Ines Kahnwald", []))

    # Nielsen
    characters.append(Character("Agnes Nielsen", ["Tronte Nielsen"]))
    characters.append(Character("Tronte Nielsen", ["Ulrich Nielsen", "Mads Nielsen"]))
    characters.append(Character("Jana Nielsen", ["Ulrich Nielsen", "Mads Nielsen"]))
    characters.append(Character("Mads Nielsen", []))
    characters.append(Character("Ulrich Nielsen", ["Martha Nielsen", "Mikkel Nielsen", "Magnus Nielsen"]))
    characters.append(Character("Katharina Nielsen", ["Martha Nielsen", "Mikkel Nielsen", "Magnus Nielsen"]))
    characters.append(Character("Mikkel Nielsen", ["Jonas Kahnwald"]))
    characters.append(Character("Martha Nielsen", []))
    characters.append(Character("Magnus Nielsen", []))

    # Albers
    characters.append(Character("Hermann Albers", ["Katharina Nielsen"]))
    characters.append(Character("Helene Albers", ["Katharina Nielsen"]))

    # Other
    characters.append(Character("Anatol Veliev", []))
    characters.append(Character("Ulla Schmidt", ["Peter Doppler"]))
    characters.append(Character("Sebastian Kruger", ["Hannah Kahnwald"]))
    characters.append(Character("Noah", ["Charlotte Doppler"]))
    characters.append(Character("Silja", ["Noah", "Agnes Nielsen"]))

    self.characters = characters

# for character in characters:
#   print(f"nome: {character.name}")
#   print(f"filhos: {character.sons}")


