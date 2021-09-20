from typing import List


def maior_elemento(lista: List):

    i = 1
    maiorValor = lista[0]

    while i <= len(lista) - 1:

        if lista[i] > maiorValor:
            maiorValor = lista[i]

        i += 1

    return maiorValor


def test_maior_elemento():

    lista = [2, 4, 2, 2, 3, 3, 1]

    if (maior_elemento(lista) == 4):
        print('ok inverte_lista([2, 4, 2, 2, 3, 3, 1])')
    else:
        print('not ok inverte_lista() expected: 4 actual: ',
              maior_elemento(lista))


test_maior_elemento()
