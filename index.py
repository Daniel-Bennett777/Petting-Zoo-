'''This module defines all classes of animals.'''
from attractions import PettingZoo, SnakePit, Wetlands
from animals import Clownfish, Dolphin, Goldfish, Seahorse, Turtle
from animals import Anaconda, BoaConstrictor, GarterSnake, KingSnake, Python
from animals import Donkey, Goat, Horse, Llama, Pig, Goose, Alligator




#walking properties keys (name, species, shift)
# prints Roberto the alpaca is available to pet during the midday shift.
# Create attractions
varmint_village = PettingZoo("Varmint Village", "cute and fuzzy critters to cuddle")
slither_inn = SnakePit("Slither Inn", "stupendous snakes of all sizes")
wetlands_reserve = Wetlands("Wetlands Reserve", "aquatic creatures of all kinds")

# Create animals
porky = Pig("Porky", "domestic pig", "morning", "corn", 123)
mama = Llama("Mama", "alpaca", "midday", "wheat pellets", 12384)
studly = Horse("studly", "paint mixed horse", "evening", "oats", 675)
oochie = Goat("oochie", "billy goat nubian", "midday", "wheat pellets", 8464)
slapper = Donkey("slapper", "Donkey", "morning", "oats", 756)
sheller = Turtle("sheller", "Pacific hard shell turtle", "lettuce", 67575)
little = Seahorse("little", "atlantic coast seahorse", "plankton", 5656)
goldy = Goldfish("goldy", "domestic goldfish hybrid", "dehydrated seaweed", 123789)
dolly = Dolphin("dolly", "gulf coast dolphin", "finger mullets", 546)
clowner = Clownfish("clowner", "gulf reef clownfish", "dehydrated seaweed", 4634636)
slinky = Python("slinky", "florida native python", "rats", 63463)
king = KingSnake("king", "arabian king snake", "rats", 46346)
gaston = GarterSnake("gaston", "middle tennessee garter snake", "rats", 43463)
tightly = BoaConstrictor("tightly", "South American Boa", "rats", 4636377)
tightest = Anaconda("tightest", "South American Anaconda", "rats", 78876)
bob = Goose("Bob", "Canada goose", "watercress sandwiches", 768986)
snappy = Alligator("Snappy", "American Alligator", "fish", 1044)

# Assign critters to PettingZoo
varmint_village.add_animal_pythonic(porky)
varmint_village.add_animal_pythonic(mama)
varmint_village.add_animal_pythonic(studly)
varmint_village.add_animal_pythonic(oochie)
varmint_village.add_animal_pythonic(slapper)



# Assign critters to SnakePit
slither_inn.add_animal_pythonic(slinky)
slither_inn.add_animal_pythonic(king)
slither_inn.add_animal_pythonic(gaston)
slither_inn.add_animal_pythonic(tightly)
slither_inn.add_animal_pythonic(tightest)

# Assign critters to Wetlands
wetlands_reserve.add_animal_pythonic(sheller)
wetlands_reserve.add_animal_pythonic(little)
wetlands_reserve.add_animal_pythonic(goldy)
wetlands_reserve.add_animal_pythonic(dolly)
wetlands_reserve.add_animal_pythonic(clowner)
wetlands_reserve.add_animal_pythonic(snappy)

# Create a list of attractions
attractions = [varmint_village, slither_inn, wetlands_reserve]

# Print attraction details
for attraction in attractions:
    print(f'{attraction.attraction_name} is where you\'ll find {attraction.description}, like')
    for animal in attraction.animals:
        print(f'   * {animal.name} the {animal.species}')

# Test Goose
bob.run()
bob.swim()

# Print the animals in PettingZoo after attempting to add Bob
print("Animals in PettingZoo:")
for animal in varmint_village.animals:
    print(f'   * {animal.name} the {animal.species}')



# Print the animals in each attraction
print("Animals in PettingZoo:")
for animal in varmint_village.animals:
    print(f'   * {animal.name} the {animal.species}')

print("Animals in SnakePit:")
for animal in slither_inn.animals:
    print(f'   * {animal.name} the {animal.species}')

print("Animals in Wetlands:")
for animal in wetlands_reserve.animals:
    print(f'   * {animal.name} the {animal.species}')
