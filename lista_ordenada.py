def ordenada(lista):

    i = 0
    while (i < len(lista)-1):
        i += 1
        if(lista[i] < lista[i-1]):
            return False

    return True


lista = [-100, 1, 2, 3, 4, 100]
print(ordenada(lista))

lista = [1, 2, 3, 4, 100, -100]
print(ordenada(lista))
