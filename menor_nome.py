def menor_nome(lista_nomes):

    nome_menor = ''

    for nome in lista_nomes:

        nome = nome.strip()
        nome = nome.capitalize()

        if(len(nome) < len(nome_menor)) or (nome_menor == ''):
            nome_menor = nome

    return nome_menor
