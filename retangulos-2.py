

# digite a largura: 10
# digite a altura: 3
# ##########
# #        #
# ##########

largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))
i = j = 1

while(j <= altura):
    while(i <= largura):
        if ((j == 1) or (j == altura)) or ((i == 1) or (i == largura)):
            print('#', end='')
        else:
            print(' ', end='')
        i += 1

    print()
    j += 1
    i = 1
