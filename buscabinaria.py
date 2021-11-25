
def busca_binaria(n, lista):

    # print()
    # print('Tamanho da lista:', len(lista), '. Número para achar:', n, '. Índice do número:', lista.index(n),
    #       '. Lista:', lista)

    inicio = 0
    fim = len(lista)
    tam = fim + inicio

    if (tam % 2 == 0):
        meio = int(tam / 2)
    else:
        meio = int((tam + 1) / 2)

    if fim == 1:
        meio = 0
    while(lista[meio] != n):
        # print('Teste meio:', meio, '. Valor do indice:', lista[meio])

        if(n < lista[meio]):
            fim = meio

        elif(n > lista[meio]):
            inicio = meio

        tam = fim + inicio
        meio = int(tam / 2)

    return(meio)


# busca_binaria(8)


def test_busca_binaria():
    lista = [11]
    # lista = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    for i in lista:
        if(busca_binaria(i, lista) == lista.index(i)):
            print('ok', i)
        else:
            print('not ok for indice: ', i)


test_busca_binaria()
