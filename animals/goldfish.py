from datetime import date

from .animal import Animal

class Goldfish(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swim_speed = 3

    def feed(self):
        '''feeding function'''
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        '''String representation of this animal object'''
        return f"{self.name} is a {self.species} and eats {self.food}"

    @property
    def chip_number(self):
        return self.__chip_number

    @chip_number.setter
    def chip_number(self, number):
        pass  # Do nothing to prevent changes
    