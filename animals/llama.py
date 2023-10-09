'''LLAMA DOC'''
from animal import Animal



class Llama(Animal):

    # Remove redundant properties from Llama's initialization, and set their values via Animal
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift  # Unique to Llama
        self.walking = True  # Unique to Llama
    
        
