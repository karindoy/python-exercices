
def bubble_sort(lista):

    i = 0
    j = 1
    x = len(lista)

    while x != 0:
        while j < len(lista):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
                print(lista)
            j += 1
            i += 1

        x -= 1
        i = 0
        j = 1

    return lista
