from random import randrange


def lista_grande(n):
    lista = []
    while(n > 0):
        lista.append(randrange(100))
        n -= 1
    return lista


print(lista_grande(8))
