def soma_lista(lista):

    if(len(lista) == 1):
        return lista[0]

    ultimo_idx = len(lista) - 1
    ultimo_valor = lista[ultimo_idx]
    lista.pop()
    lista[0] += ultimo_valor

    return soma_lista(lista)

# O resultado dos testes com seu programa foi:

# ***** [1.0 pontos]: Checando soma da lista ([1, 2]) - Falhou *****
# AssertionError: Expected 3 but got None

# ***** [1.0 pontos]: Checando soma da lista ([2, 2, 2, 2, 2]) - Falhou *****
# AssertionError: Expected 10 but got None

# ***** [1.0 pontos]: Checando soma da lista ([10101, 1000]) - Falhou *****
# AssertionError: Expected 11101 but got None

# ***** [1.0 pontos]: Checando soma da lista ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9]) - Falhou *****
# AssertionError: Expected 64 but got None
