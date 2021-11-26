def dimensoes(matriz):
    i = len(matriz[0])
    j = len(matriz)

    print(str(j)+"X"+str(i))


def test_dimensoes():
    if dimensoes([[1], [2], [3]]) == '3X1':
        print('ok for  dimensoes([[1], [2], [3]])')
    else:
        print('not ok  dimensoes([[1], [2], [3]])')

    if dimensoes([[1, 2, 3], [4, 5, 6]]) == '2X3':
        print('ok for dimensoes([[1, 2, 3], [4, 5, 6]])')
    else:
        print('not ok for dimensoes([[1, 2, 3], [4, 5, 6]])')


test_dimensoes()
