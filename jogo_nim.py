placarDoJogador = 0
placarDoComputador = 0


def computador_escolhe_jogada(n, m):  # 20 8

    # if(n - pecasTirar  % (m + 1) == 0) usuario

    # n = (n - m) % (m + 1) == 0
    pecasTirar = m
    if n < m:
        pecasTirar = n

    while(not (n - pecasTirar) % (m + 1) == 0):
        pecasTirar -= 1

        if (pecasTirar == 0):
            return m

    return pecasTirar


def usuario_escolhe_jogada(n, m):

    éNumeroValido = False

    while(not éNumeroValido):
        pecasTirar = int(input('Quantas peças você vai tirar? '))

        if(pecasTirar <= m) and (pecasTirar <= n) and (pecasTirar >= 1):
            éNumeroValido = True
        else:
            print('Oops! Jogada inválida! Tente de novo.')
    return pecasTirar


def situacaoJogo(éVezDoJogador, n, pecasTirar):

    if(pecasTirar >= 1):
        print(jogadorDaVez(éVezDoJogador), 'tirou uma peça.')
    elif(pecasTirar == 1):
        print(jogadorDaVez(éVezDoJogador), 'tirou', pecasTirar, 'peças.')

    if(n > 1):
        print('Agora restam', n, 'peças no tabuleiro.')
    elif(n == 1):
        print('Agora resta apenas uma peça no tabuleiro.')


def jogadorDaVez(éVezDoJogador):

    if(éVezDoJogador):
        jogadorDaVez = 'Você'
    else:
        jogadorDaVez = 'O computador'

    return jogadorDaVez


def partida():

    global placarDoJogador
    global placarDoComputador

    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    éVezDoJogador = False

    if(n % (m + 1) == 0):
        print('Você começa!')
        éVezDoJogador = True
        pecasTirar = usuario_escolhe_jogada(n, m)
    else:
        print('Computador começa!')
        pecasTirar = computador_escolhe_jogada(n, m)

    n = n - pecasTirar
    situacaoJogo(éVezDoJogador, n, pecasTirar)

    while(n > 0):

        if(éVezDoJogador):
            éVezDoJogador = False
            pecasTirar = computador_escolhe_jogada(n, m)
        else:
            éVezDoJogador = True
            pecasTirar = usuario_escolhe_jogada(n, m)

        n = n - pecasTirar
        situacaoJogo(éVezDoJogador, n, pecasTirar)

    print('Fim do jogo!', jogadorDaVez(éVezDoJogador), 'ganhou!')

    if(éVezDoJogador):
        placarDoJogador += 1
    else:
        placarDoComputador += 1


def main():

    tipoDeJogo = int(input('Bem-vindo ao jogo do NIM! Escolha: \n' +
                           '1 - para jogar uma partida isolada \n' +
                           '2 - para jogar um campeonato '))

    if(tipoDeJogo == 1):
        print('Voce escolheu uma partida isolada!')
        partida()
    elif(tipoDeJogo == 2):

        i = 1

        print('Voce escolheu um campeonato!')

        while (i <= 3):
            print('**** Rodada', i, '****')
            partida()
            i += 1

        print('**** Final do campeonato! ****')
        print('Placar: Você 0 X 3 Computador')


def test_computador_escolhe_jogada():

    if(computador_escolhe_jogada(3, 1) == 1):
        print('ok for computador_escolhe_jogada(3, 1)')
    else:
        print('not ok for computador_escolhe_jogada(3, 1)')

    if(computador_escolhe_jogada(1, 2) == 1):
        print('ok for computador_escolhe_jogada(1, 2)')
    else:
        print('not ok for computador_escolhe_jogada(1, 2)')

    if(computador_escolhe_jogada(2, 3) == 2):
        print('ok for computador_escolhe_jogada(2, 3)')
    else:
        print('not ok for computador_escolhe_jogada(2, 3)')

    if(computador_escolhe_jogada(14, 4) == 4):
        print('ok for computador_escolhe_jogada(14, 4)')
    else:
        print('not ok for computador_escolhe_jogada(14, 4)')

    if(computador_escolhe_jogada(13, 4) == 3):
        print('ok for computador_escolhe_jogada(13, 4))')
    else:
        print('not ok for computador_escolhe_jogada(13, 4)')

    if(computador_escolhe_jogada(2, 2) == 2):
        print('ok for computador_escolhe_jogada(2, 2))')
    else:
        print('not ok for computador_escolhe_jogada(2, 2)')

    if(computador_escolhe_jogada(6, 2) == 2):
        print('ok for computador_escolhe_jogada(6, 2))')
    else:
        print('not ok for computador_escolhe_jogada(6, 2)')

    if(computador_escolhe_jogada(15, 4) == 4):
        print('ok for computador_escolhe_jogada(15, 4))')
    else:
        print('not ok for computador_escolhe_jogada(15, 4)')

    if(computador_escolhe_jogada(25, 25) == 25):
        print('ok for computador_escolhe_jogada(25, 25))')
    else:
        print('not ok for computador_escolhe_jogada(25, 25)')

    if(computador_escolhe_jogada(11, 4) == 1):
        print('ok for computador_escolhe_jogada(11, 4))')
    else:
        print('not ok for computador_escolhe_jogada(11, 4)')


def test_usuario_escolhe_jogada():

    if(usuario_escolhe_jogada(2, 1) == 1):
        print('ok for usuario_escolhe_jogada(2, 1)')
    else:
        print('not ok for usuario_escolhe_jogada(2, 1)')

    if(usuario_escolhe_jogada(3, 2) == 2):
        print('ok for usuario_escolhe_jogada(3, 2)')
    else:
        print('not ok for usuario_escolhe_jogada(3, 2)')

    if(usuario_escolhe_jogada(4, 3) == 2):
        print('ok for usuario_escolhe_jogada(2, 3)')
    else:
        print('not ok for usuario_escolhe_jogada(2, 3)')

    if(usuario_escolhe_jogada(5, 3) >= 0):
        print('ok for usuario_escolhe_jogada(2, 3)')
    else:
        print('not ok for usuario_escolhe_jogada(2, 3)')


test_computador_escolhe_jogada()
# test_usuario_escolhe_jogada()

main()
