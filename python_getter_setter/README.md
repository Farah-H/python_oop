# Getter and Setter


__In __init__ we can make private variables, these variables are inaccessible by instances. This is done when we dont want someone to edit our variable maybe, and we want it to remain the same as when you instanced it. Or maybe you just dont want people to have access to the original formatted data in your variables ,etc.__ 

__So we use @property this makes the function that it's attached to, to act like a variable. What that means is that the function only takes in self as an argument and returns the final data you want the user to see.__

[Source](https://github.com/deviljin112/Python-OOP-Task3)

# Step 1: create a class called Student
```python
class Student():
    def __init__(self,name,company):
        self.name = name
        self.company = company
    
    def getStudent(self,value):
        self.__name # __ are used to hide the data

    def setStudent(self,value):
        self.__name = value

student_object = Student('Shahrukh', 'Sparta Global')

print(f'student name is {student_object.setStudent()}')
```

# Step 2: second iteration

```python

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
```


