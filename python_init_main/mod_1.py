# using __name__ and __main__ 

print('this is mod_1 name:' + __name__)

def main():
    pass # helps pass without an error

# Syntax is __name__ == __main__:

if __name__ == '__main__':  # it checks whether the code is run from current file
    main()