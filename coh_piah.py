import re


def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +
                      " (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def obter_tamanho_medio_das_palavras(texto):

    texto = re.sub('[.,!@#$%*():]', "", texto)
    print(texto)
    listaDePalavras = separa_palavras(texto)
    tamanhoPalavras = 0

    for palavra in listaDePalavras:
        tamanhoPalavras += len(palavra)

    print(listaDePalavras)
    print(tamanhoPalavras)

    return round(tamanhoPalavras/len(listaDePalavras), 1)


def obter_relacao_typen_token(texto):
    listaDePalavras = separa_palavras(texto)
    typenToken = n_palavras_diferentes(listaDePalavras)/len(listaDePalavras)
    return round(typenToken, 1)


def obter_relacao_hapax_legomana(texto):

    listaDePalavras = separa_palavras(texto)
    hapax = n_palavras_unicas(listaDePalavras)/len(listaDePalavras)
    return round(hapax, 2)


def obter_media_de_caracteres__da_sentenca(texto):
    return 0


def obter_complexidade_da_sentenca(texto):
    return 0


def obter_media_de_caracteres_da_frase(texto):
    return 0


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    pass


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    mediaDasPalavras = obter_tamanho_medio_das_palavras(texto)
    relacaoTypenToken = obter_relacao_typen_token(texto)
    razao_hapax_legomana = obter_relacao_hapax_legomana(texto)
    mediaDeCaractDaSentenca = obter_media_de_caracteres__da_sentenca(texto)
    complexidade_da_sentenca = obter_complexidade_da_sentenca(texto)
    mediaDeCaractDaFrase = obter_media_de_caracteres_da_frase(texto)

    pass


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    pass


# le_assinatura()
# le_textos()


def test_obter_tamanho_medio_das_palavras():

    texto = 'O gato caçava o rato, mas o rato fugiu.'
    texto2 = 'O gato caçava o rato.'

    mediaDasPalavras = obter_tamanho_medio_das_palavras(texto)
    relacaoTypenToken = obter_relacao_typen_token(texto2)
    razao_hapax_legomana = obter_relacao_hapax_legomana(texto2)
    mediaDeCaractDaSentenca = obter_media_de_caracteres__da_sentenca(texto)
    complexidade_da_sentenca = obter_complexidade_da_sentenca(texto)
    mediaDeCaractDaFrase = obter_media_de_caracteres_da_frase(texto)

    expectedMediaDasPalavras = 3.2
    expectedRelacaoTypenToken = 0.8
    expectedRazao_hapax_legomana = 0.6
    expectedMediaDeCaractDaSentenca = 29
    expectedComplexidade_da_sentenca = 1
    expectedMediaDeCaractDaFrase = 29

    valoresTestes = [[mediaDasPalavras, expectedMediaDasPalavras],
                     [relacaoTypenToken, expectedRelacaoTypenToken],
                     [razao_hapax_legomana, expectedRazao_hapax_legomana],
                     [mediaDeCaractDaSentenca, expectedMediaDeCaractDaSentenca],
                     [complexidade_da_sentenca, expectedComplexidade_da_sentenca],
                     [mediaDeCaractDaFrase, expectedMediaDeCaractDaFrase]]

    i = 0

    while(i <= (len(valoresTestes) - 1)):

        if valoresTestes[i][1] == valoresTestes[i][0]:
            print('ok for', valoresTestes[i][1], ' == ', valoresTestes[i][0])
        else:
            print('expected: ', valoresTestes[i][1],
                  ' actual: ', valoresTestes[i][0])

        i += 1


test_obter_tamanho_medio_das_palavras()
