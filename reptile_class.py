# creating a reptile class as a child class of our Animal class
from animal_class import Animal
# syntax to import files and classes

class Reptile(Animal):

    # initialising Reptile Class
    def __init__(self):
    
        super().__init__() # `super` key word is used to inherit everything from a parent class.

        self.cold_blooded = True
        self.tetrapod = True
        self.heart_chamber = [3, 4]

    def seek_heat(self):
        return 'It\'s feezing, looking for sunshine.'
    
    def hunt(self):
        return 'working really hard to catch a meal.'
        
    def use_venom(self):
        return "Bite!"

    def attract_mate_through_scent(self):
        return "walk around, showers not allowed"