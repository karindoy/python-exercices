n = input('Digite um número inteiro: ')
lenghtN = len(n)
n = int(n)

somaN = 0
i = 0
while i < lenghtN :
    lastNumber =  n % 10 
    somaN = somaN + lastNumber
    n = n // 10
    i+=1

print(somaN)