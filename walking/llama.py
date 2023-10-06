'''LLAMA DOC'''
from datetime import date

class Llama:
    '''Llama Object'''
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.walking = True
        self.food = food
    def feed(self):
        '''Function for feeding'''
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        '''String representation of this animal object'''
        return f"{self.name} is a {self.species} on the {self.shift} shift and eats {self.food}"
