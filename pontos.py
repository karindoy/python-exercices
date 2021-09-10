import math
# d(x,y)=(x1​−x2​)2+(y1​−y2​)2
p1x = int(input('Digite o x de ponto p1: '))
p1y = int(input('Digite o y de ponto p1: '))
p2x = int(input('Digite o x de ponto p2: '))
p2y = int(input('Digite o y de ponto p2: '))

d = math.sqrt(((p1x - p2x) ** 2) + ((p1y - p2y) ** 2))
if (d >= 10 ): 
    print('longe')
else:
    print('perto')    