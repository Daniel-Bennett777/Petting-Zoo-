'''kingsnake'''
from datetime import date

class KingSnake:
    '''KINGSNAKE'''
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        