# Using getter and setter functions
    
class Student():
    def __init__(self,name,value):
        self.name = name
        self.company = company

    @property # a decorator in python is any callable python object that is used to modify a funciton or a class 
    def Student(self, value):
        print('This setter method in student data')
        self.__name # __ are used to hide the data
    
    @student.setter
    def Student(self,value):
        print('calling @student.student method')
        self.__name = value

student_object = Student('Shahrukh', 'Sparta Global')
