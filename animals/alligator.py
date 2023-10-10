from movements import Walking, Swimming
from .animal import Animal


class Alligator(Animal, Walking, Swimming):

    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
        Walking.__init__(self)
        Walking.__init__(self)
        self.walk_speed = 1
        self.swim_speed = 2
