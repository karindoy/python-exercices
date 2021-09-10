import math
a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

delta =  (b ** 2) - 4 * a * c

print(delta)
if (delta >= 0 ):
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    if(delta > 0 ):
            if (x1 < x2):   
                print('as raízes da equação são', x1 ,'e', x2)
            else: 
                print('as raízes da equação são', x2 ,'e', x1)
    elif(delta == 0):   
        print('a raiz dupla desta equação é', x1)        
else:    
    print('esta equação não possui raízes reais')
