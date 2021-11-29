def sao_multiplicaveis(m1, m2):

    m1_i = len(m1)
    m1_j = len(m1[0])

    m2_i = len(m2)
    m2_j = len(m2[0])

    if (m1_j == m2_i):
        return True
    else:
        return False


def test_sao_multiplicaveis():

    m1 = [[1], [2], [3]]
    m2 = [[1, 2, 3]]

    if sao_multiplicaveis(m1, m2) == True:
        print('ok for  sao_multiplicaveis(m1, m2)')
    else:
        print('not ok  sao_multiplicaveis(m1, m2)')

    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = [[2, 3, 4], [5, 6, 7]]

    if sao_multiplicaveis(m1, m2) == False:
        print('ok for  sao_multiplicaveis(m1, m2)')
    else:
        print('not ok  sao_multiplicaveis(m1, m2)')

    m1 = [[1]]
    m2 = [[2, 3, 4]]

    if sao_multiplicaveis(m1, m2) == True:
        print('ok for  sao_multiplicaveis(m1, m2)')
    else:
        print('not ok  sao_multiplicaveis(m1, m2)')


test_sao_multiplicaveis()
