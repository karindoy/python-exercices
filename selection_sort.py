
def ordena(lista):

    idx = 0

    while (idx < (len(lista))):
        j = idx+1

        while(j < (len(lista))):
            if (lista[idx] > lista[j]):
                lista[idx], lista[j] = lista[j], lista[idx]
            j += 1

        idx += 1

    return lista


print(ordena([1, 85, 63, 69, 52, 45, 55, 87, -22]))
