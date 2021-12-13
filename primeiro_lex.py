def primeiro_lex(lista):

    e_menor_lex = ''

    for e in lista:
        if (e_menor_lex == '') or (e < e_menor_lex):
            e_menor_lex = e

    return e_menor_lex


# print(primeiro_lex(['oĺá', 'A', 'a', 'casa']))
# # deve devolver 'A'

# print(primeiro_lex(['AAAAAA', 'b']))
# # deve devolver 'AAAAAA'
