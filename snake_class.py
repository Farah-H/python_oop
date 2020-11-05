# creating snake class as child class of reptile
from reptile_class import Reptile

class Snake(Reptile):

    def __init__(self):

        super().__init__() # inheriting things from parent class

        self.forked_tongue = True
        self.venom = True
        self.limbs = False

    # creating functions for our snake class
    def use_tongue_to_smell(self):
        return 'I use tongue to smell'


