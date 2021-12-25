def insertion_sort(lista):
    i = 1

    while(i < len(lista)):
        j = i - 1
        x = i

        while(j >= 0) and (lista[j] > lista[x]):

            lista[x], lista[j] = lista[j], lista[x]

            j -= 1
            x -= 1
        i += 1
        print(lista)

    return lista


# insertion_sort([6, 5, 3, 1, 8, 7, 2, 4])
