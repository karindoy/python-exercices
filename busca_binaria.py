
def busca(lista, n):

    idx_inicio = 0
    idx_meio = len(lista)//2
    idx_fim = len(lista) - 1

    while(idx_meio != len(lista)):
        print(idx_meio)
        if lista[idx_meio] == n:
            return idx_meio
        else:
            if(n > lista[idx_meio]):
                idx_inicio = idx_meio
                idx_fim = idx_fim
                idx_meio = (idx_fim - idx_inicio)//2
                if idx_meio == 0:
                    idx_meio += 1

                idx_meio = idx_inicio + (idx_meio)

            else:
                idx_inicio = idx_inicio
                idx_fim = idx_meio
                idx_meio = (idx_fim - idx_inicio)//2
                idx_meio = idx_inicio + (idx_meio)

    return False
