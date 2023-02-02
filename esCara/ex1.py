class Forma():

    def area():
        pass

    def perimetro():
        pass

class Triangolo():

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def tipo(self):
        if self.a==self.b and self.a==self.c:
            print('Il triangolo è eqilatero')
        elif self.a==self.b or self.a==self.c or self.b==self.c:
            print('Il triangolo è isoscele')
        else:
            print('Il triangolo è scaleno')

    def perimetro

class Rettangolo():

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def tipo(self):
        if self.a==self.b:
            print('Quadrato')
        else:
            print('Rettangolo')

class Cerchio():

    def __init__(self, r):
        self.r = r
