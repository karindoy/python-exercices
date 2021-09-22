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

    listaDePalavras = 0
    tamanhoPalavras = 0

    for sentenca in separa_sentencas(texto):
        for frase in separa_frases(sentenca):
            for palavra in separa_palavras(frase):
                tamanhoPalavras += len(palavra)
                listaDePalavras += 1

    return tamanhoPalavras/listaDePalavras


def obter_relacao_typen_token(texto):

    listaDePalavras = []

    for sentenca in separa_sentencas(texto):
        for frase in separa_frases(sentenca):
            listaDePalavras = listaDePalavras + separa_palavras(frase)
    print(listaDePalavras)
    typenToken = n_palavras_diferentes(listaDePalavras)/len(listaDePalavras)
    return typenToken


def obter_relacao_hapax_legomana(texto):
    listaDePalavras = []
    for sentenca in separa_sentencas(texto):
        for frase in separa_frases(sentenca):
            listaDePalavras = listaDePalavras + separa_palavras(frase)

    hapax = n_palavras_unicas(listaDePalavras)/len(listaDePalavras)
    return hapax


def obter_media_de_caracteres__da_sentenca(texto):

    listaSentencas = separa_sentencas(texto)
    qtddDeCaracteres = 0

    for sentenca in listaSentencas:
        qtddDeCaracteres += len(sentenca)

    return qtddDeCaracteres/len(listaSentencas)


def obter_complexidade_da_sentenca(texto):

    listaSentencas = separa_sentencas(texto)
    n_frases = 0

    for sentenca in listaSentencas:

        n_frases += len(separa_frases(sentenca))

    return n_frases/len(listaSentencas)


def obter_media_de_caracteres_da_frase(texto):
    listaSentencas = separa_sentencas(texto)
    qtddDeCaracteres = 0
    n_frases = 0

    for sentenca in listaSentencas:
        for frase in separa_frases(sentenca):

            qtddDeCaracteres += len(frase)
            n_frases += 1

    return qtddDeCaracteres/n_frases


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    i = 0
    soma = 0

    while i < 5:
        soma += abs(as_a[i] - as_b[i])
        i += 1

    return soma/6


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''

    mediaDeCaractDaSentenca = obter_media_de_caracteres__da_sentenca(texto)
    complexidade_da_sentenca = obter_complexidade_da_sentenca(texto)
    mediaDeCaractDaFrase = obter_media_de_caracteres_da_frase(texto)

    mediaDasPalavras = obter_tamanho_medio_das_palavras(texto)
    relacaoTypenToken = obter_relacao_typen_token(texto)
    razao_hapax_legomana = obter_relacao_hapax_legomana(texto)

    return [mediaDasPalavras, relacaoTypenToken, razao_hapax_legomana,
            mediaDeCaractDaSentenca, complexidade_da_sentenca, mediaDeCaractDaFrase]


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    i = 0

    while i < (len(textos) - 1):
        assinaturaTexto = calcula_assinatura(textos[i])
        grauSimilaridade = compara_assinatura(assinaturaTexto, ass_cp)

        if (i == 0) or (grauSimilaridade < grauSimilaridadeCopiado):
            copiado = i + 1
            grauSimilaridadeCopiado = grauSimilaridade

        i += 1

    return copiado


# le_assinatura()
# le_textos()


def test_assinatura():

    texto = 'Então resolveu ir brincar com a Máquina pra ser também imperador dos filhos da mandioca. Mas as três cunhas deram muitas risadas e falaram que isso de deuses era gorda mentira antiga, que não tinha deus não e que com a máquina ninguém não brinca porque ela mata. A máquina não era deus não, nem possuía os distintivos femininos de que o herói gostava tanto. Era feita pelos homens. Se mexia com eletricidade com fogo com água com vento com fumo, os homens aproveitando as forças da natureza. Porém jacaré acreditou? nem o herói! Se levantou na cama e com um gesto, esse sim! bem guaçu de desdém, tó! batendo o antebraço esquerdo dentro do outro dobrado, mexeu com energia a munheca direita pras três cunhas e partiu. Nesse instante, falam, ele inventou o gesto famanado de ofensa: a pacova.'
    texto2 = 'Senão quando, estando eu ocupado em preparar e apurar a minha invenção, recebi em cheio um golpe de ar; adoeci logo, e não me tratei. Tinha o emplasto no cérebro; trazia comigo a idéia fixa dos doidos e dos fortes. Via-me, ao longe, ascender do chão das turbas, e remontar ao Céu, como uma águia imortal, e não é diante de tão excelso espetáculo que um homem pode sentir a dor que o punge. No outro dia estava pior; tratei-me enfim, mas incompletamente, sem método, nem cuidado, nem persistência; tal foi a origem do mal que me trouxe à eternidade. Sabem já que morri numa sexta-feira, dia aziago, e creio haver provado que foi a minha invenção que me matou. Há demonstrações menos lúcidas e não menos triunfantes. Não era impossível, entretanto, que eu chegasse a galgar o cimo de um século, e a figurar nas folhas públicas, entre macróbios. Tinha saúde e robustez. Suponha-se que, em vez de estar lançando os alicerces de uma invenção farmacêutica, tratava de coligir os elementos de uma instituição política, ou de uma reforma religiosa. Vinha a corrente de ar, que vence em eficácia o cálculo humano, e lá se ia tudo. Assim corre a sorte dos homens.'
    texto3 = 'Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.'

    assinatura = calcula_assinatura(texto)
    assinatura2 = calcula_assinatura(texto2)
    assinatura3 = calcula_assinatura(texto3)

    mediaDeCaractDaSentenca = obter_media_de_caracteres__da_sentenca(texto)
    complexidade_da_sentenca = obter_complexidade_da_sentenca(texto)
    mediaDeCaractDaFrase = obter_media_de_caracteres_da_frase(texto)

    mediaDasPalavras = obter_tamanho_medio_das_palavras(texto)
    relacaoTypenToken = obter_relacao_typen_token(texto)
    razao_hapax_legomana = obter_relacao_hapax_legomana(texto)

    expectedMediaDasPalavras2 = 4.471
    expectedMediaDasPalavras3 = 4.507

    expectedMediaDasPalavras = 4.507142857142857
    expectedRelacaoTypenToken = 0.6928571428571428
    expectedRazao_hapax_legomana = 0.55
    expectedMediaDeCaractDaSentenca = 70.81818181818181
    expectedComplexidade_da_sentenca = 1.8181818181818181
    expectedMediaDeCaractDaFrase = 38.5
    expectedAssinatura = [4.507142857142857, 0.6928571428571428,
                          0.55, 70.81818181818181, 1.8181818181818181, 38.5]

    valoresTestes = [[mediaDasPalavras, expectedMediaDasPalavras],
                     [relacaoTypenToken, expectedRelacaoTypenToken],
                     [razao_hapax_legomana, expectedRazao_hapax_legomana],
                     [mediaDeCaractDaSentenca, expectedMediaDeCaractDaSentenca],
                     [complexidade_da_sentenca, expectedComplexidade_da_sentenca],
                     [mediaDeCaractDaFrase, expectedMediaDeCaractDaFrase],
                     [assinatura, expectedAssinatura],
                     [assinatura2[0], expectedMediaDasPalavras2],
                     [assinatura3[0], expectedMediaDasPalavras3]]

    i = 0

    while(i <= (len(valoresTestes) - 1)):

        if valoresTestes[i][1] == valoresTestes[i][0]:
            print('ok for', valoresTestes[i][1], ' == ', valoresTestes[i][0])
        else:
            print('expected: ', valoresTestes[i][1],
                  ' actual: ', valoresTestes[i][0])

        i += 1


test_assinatura()
