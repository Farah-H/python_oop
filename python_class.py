from snake_class import Snake

class Python(Snake):
    
    def __init__(self):
        super().__init__()

        self.large = True
        self.two_lungs = True
        self.venom = False

    def digest_large_prey(self):
        return 'Yummy!'

    def constrict(self):
        return 'squish!'

    def climb(self):
        return 'Up we go!'
    
    def shed_skin(self):
        return 'Time to grow up fast!'

#python_object = Python()
# creating an object from python class 
#print(Python())
#print(python_object.breathe()) # function from our Animal class 


