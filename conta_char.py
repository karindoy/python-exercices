def conta_letras(frase, tipo='vogais'):

    conta_tipo_letra = 0

    if (tipo == 'vogais'):
        for letra in frase:
            if letra.lower() in (['a', 'e', 'i', 'o', 'u']):
                conta_tipo_letra += 1
    else:
        for letra in frase:
            if letra.lower() not in (['a', 'e', 'i', 'o', 'u', ' ']):
                conta_tipo_letra += 1
    return conta_tipo_letra
