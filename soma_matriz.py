def soma_matrizes(m1, m2):

    m1_i = len(m1)
    m1_j = len(m1[0])

    m2_i = len(m2)
    m2_j = len(m2[0])

    if (m1_i == m2_i) and (m1_j == m2_j):

        soma_matriz = [[0 for x in range(m1_j)] for y in range(m1_i)]
        sum_i = 0

        while sum_i < m1_i:

            sum_j = 0

            while sum_j < m1_j:

                soma_matriz[sum_i][sum_j] = m2[sum_i][sum_j] + m1[sum_i][sum_j]

                sum_j += 1

            sum_i += 1
        return soma_matriz
    else:
        return False


def test_soma_matrizes():

    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = [[2, 3, 4], [5, 6, 7]]

    if soma_matrizes(m1, m2) == [[3, 5, 7], [9, 11, 13]]:
        print('ok for  soma_matrizes(m1, m2)')
    else:
        print('not ok  soma_matrizes(m1, m2)')

    m1 = [[1], [2], [3]]
    m2 = [[2, 3, 4], [5, 6, 7]]

    if soma_matrizes(m1, m2) == False:
        print('ok for  soma_matrizes(m1, m2)')
    else:
        print('not ok  soma_matrizes(m1, m2)')


test_soma_matrizes()
