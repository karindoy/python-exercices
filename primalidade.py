n = int(input('Digite um número inteiro: '))

i = 1
isPrime = True
while (n > i ) & (isPrime == True) :
    if ( n % i == 0) & (i != 1):
        isPrime = False
    i+=1

if isPrime == True:
    print('primo')
else:
    print('não primo')    