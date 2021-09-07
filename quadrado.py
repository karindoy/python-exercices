# programa em Python que receba (entrada de dados) o valor correspondente ao lado de um quadrado, 
# calcule e imprima (saída de dados) seu perímetro e sua área.

larguraQuadrado = int(input('Digite o valor correspondente ao lado de um quadrado: '));

perimetro = larguraQuadrado * 4;
area = larguraQuadrado ** 2;

print('perímetro:', perimetro ,'- área:', area);