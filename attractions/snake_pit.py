from movements import Slithering
from .attraction import Attraction

class SnakePit(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)

    def add_animal_pythonic(self, animal):
        try:
            # Check if the animal has a 'swim_speed' attribute
            if hasattr(animal, 'walk_speed'):
                print(f"{animal} is a walker, so it can't be placed in {self.attraction_name}.")
                return
            # Check if the animal can walk
            if animal.slither_speed > 0:
                self.animals.append(animal)
                print(f"{animal} now lives in {self.attraction_name}")
        except AttributeError as ex:
            print(f"{animal} doesn't like to be touched, so please do not put it in the {self.attraction_name} attraction.")
   