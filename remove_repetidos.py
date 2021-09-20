from typing import List


def remove_repetidos(lista: List):

    lista.sort()
    i = 1

    while i <= (len(lista) - 1):

        if (lista[i - 1] == lista[i]):
            lista.pop(i)
        else:
            i += 1

    return lista


def test_remove_repetidos():

    lista = [2, 4, 2, 2, 3, 3, 1]

    if (remove_repetidos(lista) == [1, 2, 3, 4]):
        print('ok remove_repetidos([2, 4, 2, 2, 3, 3, 1])')
    else:
        print('not ok remove_repetidos() expected: [1, 2, 3, 4] actual: ',
              remove_repetidos(lista))


test_remove_repetidos()
