from typing import List


def soma_elementos(lista: List):

    i = 0
    sumList = 0

    while i <= (len(lista) - 1):

        sumList = lista[i] + sumList
        i += 1

    return sumList


def test_soma_elementos():

    lista = [2, 4, 2, 2, 3, 3, 1]

    if (soma_elementos(lista) == 17):
        print('ok soma_elementos_repetidos([2, 4, 2, 2, 3, 3, 1])')
    else:
        print('not ok soma_elementos() expected: 17 actual: ',
              soma_elementos(lista))


test_soma_elementos()
