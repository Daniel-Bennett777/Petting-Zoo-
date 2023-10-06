'''This module defines all classes of animals.'''
from attractions import PettingZoo, SnakePit, Wetlands
from swimming import Clownfish, Dolphin, Goldfish, Seahorse, Turtle 
from slithering import Anaconda, BoaConstrictor, GarterSnake, KingSnake, Python
from walking import Donkey, Goat, Horse, Llama, Pig

'''create attractions'''
varmint_village = PettingZoo("Varmint Village")
slither_inn = SnakePit("Slither Inn")
wetlands_reserve = Wetlands("Wetlands Reserve")
#walking properties keys (name, species, shift)
# prints Roberto the alpaca is available to pet during the midday shift.
'''walking'''
porky = Pig("Porky", "domestic pig", "morning", "corn")
print(porky)
mama = Llama("Mama", "alpaca", "midday", "wheat pellets")
print(mama)
studly = Horse("studly", "paint mixed horse", "evening", "oats")
print(studly)
oochie = Goat("oochie", "billy goat nubian", "midday", "wheat pellets")
print(oochie)
slapper = Donkey("slapper", "Donkey", "morning", "oats")
print(slapper)
'''Swimming'''
sheller = Turtle("sheller", "Pacific hard shell turtle", "lettuce")
print(sheller)
little = Seahorse("little", "atlantic coast seahorse", "plankton")
print(little)
goldy = Goldfish("goldy", "domestic goldfish hybrid", "dehydrated seaweed")
print(goldy)
dolly = Dolphin("dolly", "gulf coast dolphin", "finger mullets")
print(dolly)
clowner = Clownfish("clowner", "gulf reef clownfish", "dehydrated seaweed")
print(clowner)
'''slithering'''
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
