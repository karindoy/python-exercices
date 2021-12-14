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

    def semelhantes(self, t2):
        razao = t2.a / self.a

        print(razao)
        if ((self.b * razao) == t2.b):
            if ((self.c * razao) == t2.c):
                return True

        return False


t1 = Triangulo(2, 3, 5)
t2 = Triangulo(4, 6, 10)
print(t1.semelhantes(t2))
# deve devolver True
