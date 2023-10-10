'''DONKEY MODULE'''
from .animal import Animal

class Donkey(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walk_speed = 2
    def __str__(self):
        '''String representation of this animal object'''
        return f"{self.name} is a {self.species} on the {self.shift} shift and eats {self.food}"
