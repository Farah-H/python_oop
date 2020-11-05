# creating an animal class
class Animal():

    def __init__(self): # initialising the Animal class
        self.alive = True
        self.spine = True
        self.lungs = True
        self.eyes = True

    # create behavrious to stay alive
        def breathe(self):
            return 'Keep breathing to stay alive'
        
        def move(self):
            return 'move left, right, up and down'
        
        def procreate(self):
            return 'find partner'
        
        def eat(self):
            return 'nom nom nom'

# instantiate our class / create an object
# cat = Animal()
# cat as child has inherited everything from animaal
