'''dolphin'''
from datetime import date
from .animal import Animal

class Dolphin(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swim_speed = 5
    def feed(self):
        print(f'on {date.today()}, {self.name} was fed {self.food} by tossing into water for dolphin to catch')
    def __str__(self):
        '''String representation of this animal object'''
        return f"{self.name} is a {self.species} and eats {self.food}"
        