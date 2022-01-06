lista2 = []


def encontra_impares(lista):

    if(len(lista) == 0):
        return lista2

    ultimo_valor = lista[len(lista) - 1]
    if(ultimo_valor % 2 != 0):
        lista2.append(ultimo_valor)

    lista.pop()

    return encontra_impares(lista)


# print(encontra_impares([10, ]), '------- []')
# print(encontra_impares([13, ]), '------- [13]')
# print(encontra_impares([8, 4, 14]), '------- []')
# print(encontra_impares([2, 7, 4]), '------- [7]')
# print(encontra_impares([9, 3, 7]), '------- [3, 7, 9]')

# ***** [0.6 pontos]: Checando inteiros positivos ((12, 11, 4, 5, 2)) - Falhou *****
# AssertionError: Esperando:
# [5, 11]
# ---
# Encontrado:
# [1, 3, 5, 5, 11]

# ***** [0.6 pontos]: Checando inteiros positivos ((9, 4, 5, 8, 7)) - Falhou *****
# AssertionError: Esperando:
# [5, 7, 9]
# ---
# Encontrado:
# [1, 3, 5, 5, 7, 9]

# ***** [0.6 pontos]: Checando inteiros positivos ((8, 3, 4, 5)) - Falhou *****
# AssertionError: Esperando:
# [3, 5]
# ---
# Encontrado:
# [1, 3, 3, 5, 5]

# ***** [0.6 pontos]: Checando inteiros positivos ((13, 4, 5, 2)) - Falhou *****
# AssertionError: Esperando:
# [5, 13]
# ---
# Encontrado:
# [1, 3, 5, 5, 13]

# ***** [0.4 pontos]: Checando inteiros negativos e positivos ((-10,)) - Falhou *****
# AssertionError: Esperando:
# []
# ---
# Encontrado:
# [1, 3, 5]

# ***** [0.4 pontos]: Checando inteiros negativos e positivos ((-13,)) - Falhou *****
# AssertionError: Esperando:
# [-13]
# ---
# Encontrado:
# [-13, 1, 3, 5]

# ***** [0.4 pontos]: Checando inteiros negativos e positivos ((-8, 4, -14)) - Falhou *****
# AssertionError: Esperando:
# []
# ---
# Encontrado:
# [1, 3, 5]

# ***** [0.4 pontos]: Checando inteiros negativos e positivos ((-9, -3, 7)) - Falhou *****
# AssertionError: Esperando:
# [-9, -3, 7]
# ---
# Encontrado:
# [-9, -3, 1, 3, 5, 7]

# ***** [0.4 pontos]: Checando inteiros negativos e positivos ((-2, -7, -4)) - Falhou *****
# AssertionError: Esperando:
# [-7]
# ---
# Encontrado:
# [-7, 1, 3, 5]

# ***** [0.4 pontos]: Checando inteiros negativos e positivos ((-12, 11, -4, -5, 2)) - Falhou *****
# AssertionError: Esperando:
# [-5, 11]
# ---
# Encontrado:
# [-5, 1, 3, 5, 11]

# ***** [0.4 pontos]: Checando inteiros negativos e positivos ((-9, 4, 5, -8, -7)) - Falhou *****
# AssertionError: Esperando:
# [-9, -7, 5]
# ---
# Encontrado:
# [-9, -7, 1, 3, 5, 5]

# ***** [0.4 pontos]: Checando inteiros negativos e positivos ((-8, -3, 4, -5)) - Falhou *****
# AssertionError: Esperando:
# [-5, -3]
# ---
# Encontrado:
# [-5, -3, 1, 3, 5]

# ***** [0.4 pontos]: Checando inteiros negativos e positivos ((-13, 4, 5, -2)) - Falhou *****
# AssertionError: Esperando:
# [-13, 5]
# ---
# Encontrado:
# [-13, 1, 3, 5, 5]
