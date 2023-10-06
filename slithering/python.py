'''Python'''
from datetime import date
class Python:
    '''PYTHON'''
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food
    def feed(self):
        '''feeding function'''
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        '''String representation of this animal object'''
        return f"{self.name} is a {self.species} and eats {self.food}"
        