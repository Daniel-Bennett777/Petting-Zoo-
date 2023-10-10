from movements import Swimming
from .attraction import Attraction
  # Assuming you have a Swimming class for aquatic animals

class Wetlands(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)
    def add_animal_pythonic(self, animal):
        try:
            # Check if the animal has a 'walk_speed' attribute
            if hasattr(animal, 'slither_speed'):
                print(f"{animal} is a snake, so it can't be placed in {self.attraction_name}.")
                return
            # Check if the animal can swim
            if animal.swim_speed > 0:
                self.animals.append(animal)
                print(f"{animal} now lives in {self.attraction_name}")
        except AttributeError as ex:
            print(f"{animal} doesn't like to swim, so please do not put it in the {self.attraction_name} attraction.")    

    def add_animal(self, animal):
        if isinstance(animal, Swimming):
            self.animals.append(animal)
            print(f"{animal} now lives in {self.attraction_name}")
        else:
            print(f"{animal} doesn't belong in {self.attraction_name}.")
  