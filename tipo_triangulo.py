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


t = Triangulo(4, 4, 4)
print(t.tipo_lado())
# deve devolver 'equilátero'

u = Triangulo(3, 4, 5)
print(u.tipo_lado())
# deve devolver 'escaleno'
