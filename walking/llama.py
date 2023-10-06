'''LLAMA DOC'''
from datetime import date
class Llama:
    '''A class to represent llamas.'''
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.walking = True
        self.name = name
        self.species = species
        self.date_added = date.today()