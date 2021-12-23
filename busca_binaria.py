
def define_meio(tam_lista, idx_inicio):
    if(tam_lista % 2 == 0):
        meio = (tam_lista/2) + idx_inicio - 1
        return int(meio)
    else:
        meio = (tam_lista//2) + idx_inicio
        return int(meio)


def busca(lista, n):

    idx_inicio = 0
    idx_fim = len(lista) - 1
    tam_lista = (idx_fim + 1) - idx_inicio

    idx_meio = define_meio(tam_lista, idx_inicio)

    while(idx_meio != len(lista)):
        print(idx_meio)
        if lista[idx_meio] == n:
            return idx_meio
        else:
            if(n > lista[idx_meio]):
                idx_inicio = idx_meio + 1

                tam_lista = (idx_fim + 1) - idx_inicio
                if(tam_lista == 0):
                    return False

                idx_meio = define_meio(tam_lista, idx_inicio)
            else:
                idx_fim = idx_meio - 1

                tam_lista = (idx_fim + 1) - idx_inicio
                if(tam_lista == 0):
                    return False

                idx_meio = define_meio(tam_lista, idx_inicio)

    return False
