# programa em Python que recebe um número inteiro e imprime seu dígito das dezenas.

number = input('Digite um número inteiro: ')
if (len(number) > 1): 

    print('O dígito das dezenas é', number[-2])

else :
  print('O dígito das dezenas é 0')
