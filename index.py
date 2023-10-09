'''This module defines all classes of animals.'''
from attractions import PettingZoo, SnakePit, Wetlands
from swimming import Clownfish, Dolphin, Goldfish, Seahorse, Turtle
from slithering import Anaconda, BoaConstrictor, GarterSnake, KingSnake, Python
from walking import Donkey, Goat, Horse, Llama, Pig




#walking properties keys (name, species, shift)
# prints Roberto the alpaca is available to pet during the midday shift.
'''walking'''
varmint_village = PettingZoo("Varmint Village", "cute and fuzzy critters to cuddle")
porky = Pig("Porky", "domestic pig", "morning", "corn")
print(porky)
mama = Llama("Mama", "alpaca", "midday", "wheat pellets", 12384)
print(mama)
studly = Horse("studly", "paint mixed horse", "evening", "oats")
print(studly)
oochie = Goat("oochie", "billy goat nubian", "midday", "wheat pellets")
print(oochie)
slapper = Donkey("slapper", "Donkey", "morning", "oats")
print(slapper)
'''Swimming'''
wetlands_reserve = Wetlands("Wetlands Reserve", "aquatic creatures of all kinds")
sheller = Turtle("sheller", "Pacific hard shell turtle", "lettuce")
print(sheller)
little = Seahorse("little", "atlantic coast seahorse", "plankton")
print(little)
goldy = Goldfish("goldy", "domestic goldfish hybrid", "dehydrated seaweed", 123789)
print(goldy)
# This should not change the state of the object
goldy.chip_number = 555783

# But printing it should work
print(goldy.chip_number)
#prints 123789
dolly = Dolphin("dolly", "gulf coast dolphin", "finger mullets")
print(dolly)
clowner = Clownfish("clowner", "gulf reef clownfish", "dehydrated seaweed")
print(clowner)
'''slithering'''
slither_inn = SnakePit("Slither Inn", "stupendous snakes of all sizes")
slinky = Python("slinky", "florida native python", "rats")
print(slinky)
king = KingSnake("king", "arabian king snake", "rats")
print(king)
gaston = GarterSnake("gaston", "middle tennessee garter snake", "rats")
print(gaston)
tightly = BoaConstrictor("tightly", "South American Boa", "rats")
print(tightly)
tightest = Anaconda("tightest", "South American Anaconda", "rats")
print(tightest)

# Assign critters to PettingZoo
varmint_village.add_animal(porky)
varmint_village.add_animal(mama)
varmint_village.add_animal(studly)
varmint_village.add_animal(oochie)
varmint_village.add_animal(slapper)

# Assign critters to SnakePit
slither_inn.add_animal(slinky)
slither_inn.add_animal(king)
slither_inn.add_animal(gaston)
slither_inn.add_animal(tightly)
slither_inn.add_animal(tightest)
print(slither_inn.last_critter_added)

# Assign critters to Wetlands
wetlands_reserve.add_animal(sheller)
wetlands_reserve.add_animal(little)
wetlands_reserve.add_animal(goldy)
wetlands_reserve.add_animal(dolly)
wetlands_reserve.add_animal(clowner)
#create a list
attractions = [varmint_village, slither_inn, wetlands_reserve]

for attraction in attractions:
    print(f'{attraction.attraction_name} is where you\'ll find {attraction.description}, like')
    for animal in attraction.animals:
        print(f'   * {animal.name} the {animal.species}')
