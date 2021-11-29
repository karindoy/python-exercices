def imprime_matriz(matriz):

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end="")

            if j != (len(matriz[0]) - 1):
                print(" ", end="")
            j += 1

        print()
        i += 1


minha_matriz = [[1, 2, 3], [4, 5, 6]]
imprime_matriz(minha_matriz)

minha_matriz = [[1], [2], [3]]
imprime_matriz(minha_matriz)
