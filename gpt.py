# main.py
class Parent:
    def __init__(self, txt):
        self.message = txt

    def printmessage(self):
        print(self.message)

    def convertTypeSI(self, val):
        val = int(val)
        return val
    
    def converttype(self, argu):
        ctype = input('type(shortened) : ')
        if ctype == 'str':
            argu = str(argu)
            return argu
        elif ctype == 'int':
            argu = int(argu)
            return argu
        elif ctype == 'bool':
            argu = bool(argu)
            return argu
        elif ctype == 'float':
            argu = float(argu)
            return argu
        elif ctype == 'complex':
            argu = complex(argu)
            return argu
        else:
            print('There is no type of ' + str(ctype) + '. Try another type.')
            return argu

class Child(Parent):
    def __init__(self, txt):
        super().__init__(txt)

test1 = Child("Hello, and welcome!")
