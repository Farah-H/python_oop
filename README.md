# Python OOP
We are doing to create a class structure as described in this image. 
![](https://cdn.discordapp.com/attachments/767793850529087489/773856554373611560/OOP_python.png)

### Pre-Requisites 
It is easier to complete this task when using a code editor, such as Visual Studio Code or PyCharm. You must also have Python 3.7 or later installed. You can learn how to [install VSC](https://docs.microsoft.com/en-us/visualstudio/install/install-visual-studio?view=vs-2019) or [install PyCharm](https://www.jetbrains.com/help/pycharm/quick-start-guide.html) using these hyperlinks. 

## __Task 1__: create animal class as our Parent

```python
# creating an animal class
class Animal():

    def __init__(self): # initialising the Animal class
        self.alive = True
        self.spine = True
        self.lungs = True
        self.eyes = True

# create behavrious to stay alive
# we want every child to have these behaviours, which is why they're indented in the __init__
        def breathe(self):
            return 'Keep breathing to stay alive'
        
        def move(self):
            return 'move left, right, up and down'
        
        def procreate(self):
            return 'find partner'
        
        def eat(self):
            return 'nom nom nom'
```

## __Task 2__: create reptile class as the child class 
- 

## __Task 3__: create snake class as child of reptile

## __Task 4__: create a python class

## __Task 5__: create two file using `__name__` and `__main__` in both files and show the difference in outcome.

`__name__` and `__main__` are used to check if the code is run from current file/directly for different file/importing it

In a .py file named mod_1:
```python
# using __name__ and __main__ 

print('this is mod_1 name:' + __name__)

def main():
    pass # helps pass without an error

# Syntax is __name__ == __main__:

if __name__ == '__main__':  # it checks whether the code is run from current file
    main() # ==> this is mod_1 name:__main__
``` 

In a .py file named mod_2:

```python
import mod_1

print('this is mod_2 name:' + __name__)
# ==> this is mod_1 name:mod_1
# ==> this is mod_2 name:__main__
```