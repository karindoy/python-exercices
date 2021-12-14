import math


class Triangulo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        if (self.a == self.b == self.c):
            return 'equilátero'
        if (self.a == self.b) or (self.a == self.c) or (self.b == self.c):
            return 'isósceles'
        return 'escaleno'

    def retangulo(self):

        if(self.a >= self.b) and (self.a >= self.c):
            if (self.a**2 == (self.b ** 2) + (self.c ** 2)):
                return True
            else:
                return False

        elif(self.b >= self.a) and (self.b >= self.c):
            if (self.b**2 == (self.a ** 2) + (self.c ** 2)):
                return True
            else:
                return False
        else:
            if (self.c**2 == (self.a ** 2) + (self.b ** 2)):
                return True
            else:
                return False


t = Triangulo(1, 3, 5)
print(t.retangulo())
# deve devolver False

u = Triangulo(3, 4, 5)
print(u.retangulo())
# deve devolver True
