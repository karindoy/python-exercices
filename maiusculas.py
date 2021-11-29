def maiusculas(frase):

    letras_maiusculas = ''

    for c in frase:
        if(ord(c) >= ord('A')) and (ord(c) <= ord('Z')):
            letras_maiusculas += c

    return letras_maiusculas
