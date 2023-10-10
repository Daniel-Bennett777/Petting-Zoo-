'''turtle'''
from movements import Walking, Swimming
from .animal import Animal


class Turtle(Animal, Walking, Swimming):

    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
        Walking.__init__(self)
        self.swim_speed = 1
        self.walk_speed = 2
    def __str__(self):
        '''String representation of this animal object'''
        return f"{self.name} is a {self.species} and eats {self.food}"
    def run(self):
        print(f'{self} short bursts')
        