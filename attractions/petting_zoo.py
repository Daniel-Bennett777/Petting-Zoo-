'''Pettingzoo'''
class PettingZoo:
    '''petting'''
    def __init__(self, attraction_name, description):
        self.attraction_name = attraction_name
        self.description = description
        self.animals = []
    def add_animal(self, animal):
        self.animals.append(animal)
    @property
    def last_critter_added(self):
        if self.animals:
            return self.animals[-1]  # Get the last animal in the list
        else:
            return None  # Return None if the list is empty        