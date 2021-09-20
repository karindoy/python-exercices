from typing import List


def inverte_lista(lista: List):

    i = 1
    listaInvertida = []

    while i <= len(lista):

        listaInvertida.append(lista[len(lista) - i])
        i += 1

    return listaInvertida


def main():

    n = -1
    lista = []
    while n != 0:

        n = int(input('Digite um número: '))

        lista.append(n)

    for number in inverte_lista(lista):
        if number != 0:
            print(number)


def test_inverte_lista():

    lista = [2, 4, 2, 2, 3, 3, 1]

    if (inverte_lista(lista) == [1, 3, 3, 2, 2, 4, 2]):
        print('ok inverte_lista([2, 4, 2, 2, 3, 3, 1])')
    else:
        print('not ok inverte_lista() expected: 17 actual: ',
              inverte_lista(lista))


test_inverte_lista()

main()
