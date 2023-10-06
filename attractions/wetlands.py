'''wetlands area'''

class Wetlands:
    '''wetlands class'''
    def __init__(self, attraction_name, description):
        self.attraction_name = attraction_name
        self.description = description
        self.animals = []
    def add_animal(self, animal):
        self.animals.append(animal)
            