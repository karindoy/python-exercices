class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c


t = Triangulo(1, 2, 3)

print(t.a)
# deve devolver o valor do lado a do triângulo
print(t. b)
# deve devolver o valor do lado b do triângulo
print(t.c)
# deve devolver o valor do lado c do triângulo

print(t.perimetro())
# deve devolver um inteiro correspondente ao valor do perímetro do triângulo.
